# Scaffold: StormCalculusPrime + DistributedLogger

## 1. Visão Geral

Objetivo: entregar rapidamente um MVP integrado onde o *StormCalculusPrime* consome o *DistributedLogger* via um shim de sessão (CAIO), com contexto (session\_id, correlation\_id), testabilidade e base para evoluções.

Este documento serve como ponto único de referência: templates de README, script de bootstrap/testes, checklist, branches e PRs.

---

## 2. Estrutura sugerida dos repositórios

### DistributedLogger (local path: `../DistributedLogger`)

```
storm_distributed_logger/
├── __init__.py
├── context.py         # gerenciamento de contexto (thread-local / contextvars)
├── formatters.py      # ContextFormatter, JSONFormatter
├── facade.py          # LoggerFacade + helpers (with_context)
├── config.py          # (futuro) loader de YAML/ENV para handlers/níveis
└── tests/
    └── test_facade.py
```

### StormCalculusPrime

```
StormCalculusPrime/
├── caio/
│   └── session.py     # shim leve que injeta session_id e correlation_id no logger
├── example.py         # script de "hello world" consumindo o logger
├── README.md          # descrição SEO-friendly e quickstart
└── LICENSE            # licença proprietária (All Rights Reserved)
```

---

## 3. README.md template (para ambos, com variações)

````markdown
# StormCalculusPrime

**High-Performance Python SDK for Prime Number Sequence Analysis with Distributed Logging Integration.**

Advanced computational engine for factorial-based prime-like sequences, featuring modular design, session-based correlation IDs, and real-time observability powered by the DistributedLogger framework.

## Features
- Session-aware logging with correlation_id and session_id.
- Facade-based distributed logger with context injection.
- Easy extension for multiple handlers (console, file, remote).
- Testable core (logger captured in-memory for assertions).

## Quickstart
```bash
# Assumindo que DistributedLogger está ao lado e instalado editable
pip install -e ../DistributedLogger
````

```python
from caio.session import StormSession

session = StormSession("CalculusPrime", session_id="1", verbose=True)
logger = session.get_logger()
logger.info("Iniciando cálculo", sequence=42)
```

## Development Setup

```bash
# instalar dependências de dev (se houver)
# garantir que o DistributedLogger está instalado em editable:
pip install -e ../DistributedLogger

# rodar o exemplo
python example.py
```

## License

Proprietary. All rights reserved. See LICENSE.

```
```

Para o **DistributedLogger**, variante do README deve enfatizar: "Facade-based distributed logging core for Python with contextual session and correlation ID support. Easily pluggable handlers, structured output, and testable API."

---

## 4. LICENSE (proprietária) padrão

```text
Copyright (c) 2025 Sandro Regis Cardoso
All rights reserved.

This software is proprietary. Unauthorized copying, modification, distribution, or use is strictly prohibited without explicit written permission.
```

---

## 5. Script de bootstrap / test runner (`bootstrap.sh`)

```bash
#!/usr/bin/env bash
set -euo pipefail

# 1. Instala o DistributedLogger localmente (assume layout lado a lado)
pip install -e ../DistributedLogger

# 2. Execução do exemplo
python example.py

# 3. Rodar testes do DistributedLogger (assume pytest instalado ou usa unittest)
cd ../DistributedLogger
python -m unittest discover -v
```

````
Tornar executável: `chmod +x bootstrap.sh`.

---

## 6. Checklist de MVPs e integração
### DistributedLogger MVP
- [ ] Implementar `context.py` com thread-local/contextvars.  
- [ ] Implementar `formatters.py` com `ContextFormatter`.  
- [ ] Implementar `facade.py` com caching e `with_context`.  
- [ ] Escrever testes em `tests/test_facade.py` validando contexto.  
- [ ] Adicionar `LICENSE` proprietário.  
- [ ] Atualizar README com descrição e exemplos.  

### StormCalculusPrime + CAIO shim
- [ ] Criar `caio/session.py` que injeta `session_id` e `correlation_id`.  
- [ ] Escrever `example.py` demonstrando uso.  
- [ ] Instalar `DistributedLogger` em modo editable / ajustar `PYTHONPATH`.  
- [ ] Verificar output de log contém os contextos.  
- [ ] Adicionar `LICENSE` proprietário.  
- [ ] Atualizar README com quickstart e descrição.  

### Integração e fluxo
- [ ] Branch `feature/mvp-dl` no DistributedLogger com PR draft.  
- [ ] Branch `integration/caio-session-shim` em StormCalculusPrime integrada com DL.  
- [ ] Validar sessão/log via `StormSession`.  
- [ ] Criar PRs com template (issue checklist incluída).  

---

## 7. Branching strategy
- `main` — base estável (MVP corte).  
- `develop` — integração contínua intermediária.  
- `feature/mvp-dl` — implementação do DistributedLogger core.  
- `integration/caio-session-shim` — shim leve do CAIO + integração inicial (StormCalculusPrime).  
- `feature/mvp-clp` — evolução no CalculusPrime consumindo e estendendo o logger.  
- `feature/dl-extensions` — novos handlers, structured logging, config.  
- `release/v0.1-mvp` — tag de corte.  

---

## 8. Pull Request / Commit template (`.github/pull_request_template.md`)
```markdown
## Descrição
O que foi feito e por quê.

## Checklist
- [ ] Testes adicionados / atualizados
- [ ] README atualizado
- [ ] Licença confirmada
- [ ] Changelog entry (se for release)

## Dependências
- Referenciar outras PRs ou issues relacionadas.
````

---

## 9. Sugestões de próximos passos curtos

1. Finalizar e commitar o core do DistributedLogger.
2. Validar shim do StormSession com logging contextual.
3. Criar PRs draft para revisão e documentar decisões (no CHANGELOG).
4. Preparar o CAIO leve como orquestrador de sessão para a próxima fase.

---

*Fim do scaffold.*

