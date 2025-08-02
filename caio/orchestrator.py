# caio/orchestrator.py

from storm_sdk.storm_distributed_logger import StormDistributedLogger
from storm_sdk.storm_calculus_prime import StormCalculusPrime
from caio.session import StormSession  # usa a sessão existente em caio/session.py

def boot():
    logger = StormDistributedLogger(name="caio-bootstrap")
    session = StormSession("Toró de Parpites", id=1, logger=logger)
    calc = StormCalculusPrime(session=session)

    session.drop("Bootstrapped via orchestrator")
    try:
        sample = calc.compute_sample_pattern()
    except AttributeError:
        sample = "<placeholder de padrão>"
    logger.log(f"[orchestrator] sample pattern: {sample}")

    print("Orquestração inicial completa.")
    session.show()

if __name__ == "__main__":
    boot()

