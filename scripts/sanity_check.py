# scripts/sanity_check.py

from storm_sdk.storm_distributed_logger import StormDistributedLogger
from caio.session import StormSession
from storm_sdk.storm_calculus_prime import StormCalculusPrime

def main():
    print("=== Iniciando Smoke Test ===")
    logger = StormDistributedLogger(name="smoke-test")
    session = StormSession("Toró de Parpites", id=1, logger=logger)
    calc = StormCalculusPrime(session=session)

    session.drop("Smoke test integration check")
    try:
        sample = calc.compute_sample_pattern()
    except Exception as e:
        print("Erro ao calcular padrão de exemplo:", e)
        raise

    logger.log(f"Sample pattern result: {sample}")
    print("Smoke test completado com sucesso.")
    session.show()

if __name__ == "__main__":
    main()

