# Scheduling System

Um app Frappe para agendamento de compromissos entre **Seller** e **Client**, projetado para gerenciar agendamentos com facilidade e segurança.

## Funcionalidades Principais

* \*\*Cálculo automático de \*\*\`\` com base em `start_date` e `duration`.
* **Título legível** gerado automaticamente no formato `Seller: … — Client: …`.
* **Bloqueio de agendamentos sobrepostos** para um mesmo Seller.
* **Visualização em Calendar View** para melhor gerenciamento de compromissos.

## Estrutura do Projeto

```
scheduling_system/               ← raiz do app
├── pyproject.toml               ← dependências Python
├── hooks.py                     ← registro de scripts e eventos
├── modules.txt                  ← definição do módulo “Scheduling System”
├── README.md                    ← documentação do projeto
└── scheduling_system/
    ├── doctype/appointment/
    │   ├── appointment.json     ← definição do Doctype e calendar_view
    │   └── appointment.py       ← lógicas de negócio (autoname, validações, conflitos)
    └── public/js/doctype/
        └── appointment/
            └── appointment.js    ← Client Script para cálculo em tempo real
```

## Instalação

1. **Clone o repositório** dentro da pasta `apps/` do seu bench:

   ```bash
   cd ~/frappe-bench/apps
   git clone https://github.com/SEU_USUARIO/SEU_REPO.git scheduling_system
   ```

2. **Ative o modo desenvolvedor** (necessário para criar e editar Doctypes customizados):

   ```bash
   bench set-config -g developer_mode true
   ```

3. **Registre o app e crie um site novo**:

   ```bash
   cd ~/frappe-bench
   bench new-site scheduling_site
   bench --site scheduling_site install-app scheduling_system
   ```

4. **Execute migrações** para criar as tabelas e carregar o Doctype:

   ```bash
   bench --site scheduling_site migrate
   ```

5. **Recompile o front-end** e inicie o servidor de desenvolvimento:

   ```bash
   bench --site scheduling_site clear-cache
   bench build
   bench start
   ```

## Uso

* Acesse o site gerado (`http://localhost:8000` por padrão).
* No módulo **Scheduling System**, abra o Doctype **Appointment** para criar e gerenciar compromissos.

## Personalização

* **Campos**: Edite `appointment.json` para adicionar novos campos ou customizar a visualização.
* **Lógicas**: Modifique `appointment.py` para ajustar regras de validação ou nomenclatura.
* **Scripts do cliente**: Atualize `appointment.js` para comportamento interativo em tempo real.

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).
