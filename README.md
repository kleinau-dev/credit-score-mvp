# Credit Score Platform — Backend MVP

Este repositório contém o backend do MVP da plataforma de Score de Crédito, desenvolvido com foco em arquitetura sólida, segurança, compliance e escalabilidade futura.

O escopo contempla exclusivamente a camada backend, conforme definido no projeto.

---

## Visão Geral

A API fornece toda a base necessária para cálculo, versionamento e auditoria de score de crédito, incluindo autenticação, consentimento do usuário e gestão de dados financeiros.

A arquitetura foi projetada para suportar evolução futura com integrações externas, Open Banking e modelos de score mais avançados.

---

## Stack Tecnológico

- Python 3
- FastAPI
- SQLAlchemy
- Alembic
- OAuth2 + JWT
- SQLite (MVP, pronto para PostgreSQL)
- Docker / Docker Compose

---

## Funcionalidades Implementadas

- Autenticação e autorização com JWT
- Cadastro e gestão de usuários
- Gestão de consentimento do usuário (versionado)
- Registro e atualização de dados financeiros
- Motor de cálculo de score (0–1000)
- Histórico e versionamento de score
- Logs e trilha de auditoria
- Exportação de dados do usuário
- Exclusão de dados (GDPR – direito ao esquecimento)
- Padronização de erros e respostas
- Documentação automática via Swagger

---

## Arquitetura

A aplicação segue arquitetura modular, separando responsabilidades entre:
- API (controllers)
- Services (regras de negócio)
- Models (persistência)
- Security (autenticação, autorização e permissões)
- Auditoria e compliance

Documentação técnica detalhada está disponível na pasta `/docs`.

---

## Como Executar o Projeto

### Pré-requisitos
- Docker
- Docker Compose

### Subir a API

```bash
docker-compose up --build

Acessos

API: http://localhost:8000

Swagger (OpenAPI): http://localhost:8000/docs

Health Check: http://localhost:8000/health

Segurança e Compliance

Autenticação baseada em token (JWT)

Controle de acesso

Registro de auditoria de ações sensíveis

Consentimento explícito do usuário

Exportação e exclusão de dados

Base técnica alinhada às exigências do GDPR

Status do Projeto

✔ Backend MVP concluído
✔ Infraestrutura Docker pronta
✔ Documentação técnica entregue
✔ Pronto para integração com frontend ou sistemas externos