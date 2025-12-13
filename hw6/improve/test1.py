# Improvement Method (Bubble-sort style) for 1D maximization
# Comments in English as requested.

from typing import Callable, List, Tuple

def improvement_1d(
    f: Callable[[float], float],
    x0: float,
    h: float = 0.1,
    M: int = 5,
    max_passes: int = 10_000,
    tol_improve: float = 0.0,
    verbose: bool = True
) -> Tuple[float, float, int]:
    """
    Single-stage improvement method (best-as-soon-as-found), like bubble sort:
    - Neighborhood offsets: ±h, ±2h, ..., ±M*h in a fixed order.
    - Scan offsets; on the first improvement, move immediately and restart scanning.
    - Stop when a full pass yields no improvement or max_passes reached.

    Returns: (x_best, f_best, passes_used)
    """
    # Build fixed offsets in a deterministic, alternating order: +h, -h, +2h, -2h, ...
    offsets: List[float] = []
    for k in range(1, M + 1):
        offsets.append(+k * h)
        offsets.append(-k * h)

    x = float(x0)
    fx = f(x)
    passes = 0

    while passes < max_passes:
        if verbose:
            print(f"x={x:.6f} f(x)={fx:.6f} (h={h:.6f})")

        improved = False
        # Scan offsets in fixed order; adopt first improvement and restart
        for delta in offsets:
            cand = x + delta
            f_cand = f(cand)
            if f_cand > fx + tol_improve:
                x, fx = cand, f_cand
                improved = True
                break  # restart scanning from the first offset

        passes += 1
        if not improved:
            break

    return x, fx, passes


def improvement_multistage_1d(
    f: Callable[[float], float],
    x0: float,
    h0: float = 0.2,
    stages: int = 3,
    shrink: float = 0.5,
    M: int = 5,
    max_passes_per_stage: int = 2_000,
    tol_improve: float = 0.0,
    verbose: bool = True
) -> Tuple[float, float]:
    """
    Multi-stage variant:
    - Run several improvement stages.
    - After each stage, reduce step size: h <- h * shrink.
    - Returns the final (x, f(x)).
    """
    x, fx = float(x0), f(x0)
    h = float(h0)

    for s in range(stages):
        if verbose:
            print(f"\n[Stage {s+1}/{stages}] h={h:.6f}")
        x, fx, _ = improvement_1d(
            f=f,
            x0=x,
            h=h,
            M=M,
            max_passes=max_passes_per_stage,
            tol_improve=tol_improve,
            verbose=verbose
        )
        h *= shrink

    return x, fx


# Example target function (your f): f(x) = -(x - 1)^2, maximum at x=1 with value 0.
def f(x: float) -> float:
    return -1 * (x*x - 2*x + 1)

if __name__ == "__main__":
    # Single-stage
    x_best, f_best, passes = improvement_1d(f, x0=0.0, h=0.1, M=5, verbose=True)
    print(f"\nSingle-stage result: x≈{x_best:.6f}, f(x)≈{f_best:.6f}, passes={passes}")

    # Multi-stage (refines step size automatically)
    x_best, f_best = improvement_multistage_1d(
        f, x0=0.0, h0=0.2, stages=3, shrink=0.5, M=6, verbose=True
    )
    print(f"\nMulti-stage result: x≈{x_best:.6f}, f(x)≈{f_best:.6f}")
