[![Downloads](https://pepy.tech/badge/aioyookassa)](https://pepy.tech/project/aioyookassa)
[![Downloads](https://pepy.tech/badge/aioyookassa/month)](https://pepy.tech/project/aioyookassa)
[![Downloads](https://pepy.tech/badge/aioyookassa/week)](https://pepy.tech/project/aioyookassa)

![Social Preview](.github/social-preview.png)

# aioyookassa

**Асинхронная Python библиотека для работы с API YooKassa**

`aioyookassa` — это современная асинхронная библиотека для интеграции с платежным сервисом YooKassa. Библиотека предоставляет полную поддержку всех API доменов YooKassa, включая платежи, возвраты, чеки, счета, выплаты, безопасные сделки, webhooks и многое другое.

## ✨ Особенности

- 🚀 **Асинхронность** — полная поддержка `asyncio` для высокопроизводительных приложений
- 🛡️ **Типизация** — полная поддержка типов с использованием Pydantic моделей
- 🔧 **Простота** — интуитивно понятный API для быстрой интеграции
- 📚 **Документация** — подробная документация с примерами использования
- 🧪 **Тестирование** — 95% покрытие кода тестами
- ⚡ **Производительность** — оптимизированная работа с HTTP запросами
- 🎯 **Полная поддержка API** — реализованы все домены YooKassa API

## 🔗 Links

- 🎓 **Documentation:** [_CLICK_](https://aioyookassa.readthedocs.io/en/latest/)
- 🖱️ **Developer contacts:** [![Dev-Telegram](https://img.shields.io/badge/Telegram-blue.svg?style=flat-square&logo=telegram)](https://t.me/masaasibaata)
- 💝 **Support project:** [![Tribute](https://img.shields.io/badge/Support%20Project-Tribute-green.svg?style=flat-square&logo=telegram)](https://t.me/tribute/app?startapp=dzqR)

## 🐦 Dependencies

| Library  |                       Description                       |
| :------: | :-----------------------------------------------------: |
| aiohttp  | Asynchronous HTTP Client/Server for asyncio and Python. |
| pydantic |                   JSON Data Validator                   |

## 📁 Project Structure

```
aioyookassa/
├── core/                    # Core functionality
│   ├── client.py           # Main YooKassa client
│   ├── api/                # API client implementations
│   │   ├── payments.py     # Payment operations
│   │   ├── refunds.py      # Refund operations
│   │   ├── receipts.py     # Fiscal receipt operations
│   │   ├── invoices.py     # Invoice operations
│   │   ├── payment_methods.py # Payment method management
│   │   ├── payouts.py      # Payout operations
│   │   ├── self_employed.py # Self-employed operations
│   │   ├── sbp_banks.py    # SBP banks list
│   │   ├── personal_data.py # Personal data operations
│   │   ├── deals.py        # Safe deals operations
│   │   └── webhooks.py     # Webhooks management
│   ├── methods/            # API method definitions
│   └── abc/                # Abstract base classes
├── types/                  # Pydantic models and enums
├── exceptions/             # Custom exceptions
└── __init__.py            # Package exports
```

## 🚀 Quick Start

### Установка

```bash
pip install aioyookassa
```

### Базовое использование

```python
import asyncio
from datetime import datetime
from aioyookassa import YooKassa
from aioyookassa.types.payment import Money, Confirmation
from aioyookassa.types.enum import PaymentStatus, ConfirmationType, Currency
from aioyookassa.types.params import CreatePaymentParams, GetPaymentsParams

async def main():
    # Инициализация клиента
    client = YooKassa(api_key="your_api_key", shop_id=12345)

    # Создание платежа (используем Pydantic модель)
    params = CreatePaymentParams(
        amount=Money(value=100.00, currency=Currency.RUB),
        confirmation=Confirmation(type=ConfirmationType.REDIRECT, return_url="https://example.com/return"),
        description="Тестовый платеж"
    )
    payment = await client.payments.create_payment(params)

    print(f"Payment created: {payment.id}")
    print(f"Confirmation URL: {payment.confirmation.url}")

    # Получение информации о платеже
    payment_info = await client.payments.get_payment(payment.id)
    print(f"Payment status: {payment_info.status}")

    # Получение списка платежей за сегодня (используем Pydantic модель)
    today = datetime.now()
    params = GetPaymentsParams(
        created_at=today,
        status=PaymentStatus.SUCCEEDED
    )
    payments = await client.payments.get_payments(params)
    print(f"Found {len(payments.list)} successful payments today")

    # Закрытие клиента
    await client.close()

# Запуск
asyncio.run(main())
```

## 🎯 Поддерживаемые API домены

Библиотека поддерживает **все API домены YooKassa**:

- 💳 **Платежи (Payments)** — создание, подтверждение, отмена платежей
- 💰 **Возвраты (Refunds)** — полные и частичные возвраты
- 🧾 **Чеки (Receipts)** — регистрация фискальных чеков
- 📄 **Счета (Invoices)** — создание и управление счетами
- 💳 **Способы оплаты (Payment Methods)** — управление сохраненными способами оплаты
- 💸 **Выплаты (Payouts)** — выплаты на карты, через СБП, на кошельки ЮMoney
- 👤 **Самозанятые (Self-Employed)** — работа с самозанятыми получателями
- 🏦 **Участники СБП (SBP Banks)** — получение списка банков СБП
- 🔐 **Персональные данные (Personal Data)** — управление персональными данными получателей
- 🤝 **Безопасные сделки (Deals)** — создание и управление безопасными сделками
- 🔔 **Webhooks** — подписка на события, управление уведомлениями и обработка входящих webhook-уведомлений

## 📋 Основные методы

### 💳 Платежи (Payments)

```python
from datetime import datetime
from aioyookassa.types.enum import PaymentStatus, ConfirmationType, Currency
from aioyookassa.types.params import CreatePaymentParams, GetPaymentsParams

# Создание платежа (используем Pydantic модель)
params = CreatePaymentParams(
    amount=Money(value=1000.00, currency=Currency.RUB),
    confirmation=Confirmation(type=ConfirmationType.REDIRECT, return_url="https://example.com/return"),
    description="Оплата заказа #12345"
)
payment = await client.payments.create_payment(params)

# Получение списка платежей (используем Pydantic модель)
params = GetPaymentsParams(
    created_at=datetime(2023, 1, 1, 12, 0, 0),
    status=PaymentStatus.SUCCEEDED,
    limit=10
)
payments = await client.payments.get_payments(params)

# Получение конкретного платежа
payment = await client.payments.get_payment("payment_id")

# Подтверждение платежа (используем Pydantic модель)
from aioyookassa.types.params import CapturePaymentParams

params = CapturePaymentParams(amount=Money(value=1000.00, currency=Currency.RUB))
payment = await client.payments.capture_payment("payment_id", params)

# Отмена платежа
payment = await client.payments.cancel_payment("payment_id")
```

### 💰 Возвраты (Refunds)

```python
from aioyookassa.types.params import CreateRefundParams

# Создание возврата (используем Pydantic модель)
params = CreateRefundParams(
    payment_id="payment_id",
    amount=Money(value=500.00, currency=Currency.RUB),
    description="Частичный возврат"
)
refund = await client.refunds.create_refund(params)

# Получение информации о возврате
refund_info = await client.refunds.get_refund("refund_id")
```

### 🧾 Чеки (Receipts)

```python
from aioyookassa.types.payment import Customer, Settlement
from aioyookassa.types.enum import ReceiptType, PaymentSubject, PaymentMode, Currency
from aioyookassa.types.params import CreateReceiptParams
from aioyookassa.types.receipt_registration import ReceiptRegistrationItem

# Регистрация чека (используем Pydantic модель)
params = CreateReceiptParams(
    type=ReceiptType.PAYMENT,
    payment_id="payment_id",
    customer=Customer(email="customer@example.com"),
    items=[
        ReceiptRegistrationItem(
            description="Товар",
            quantity=1,
            amount=Money(value=1000.00, currency=Currency.RUB),
            vat_code=1,
            payment_subject=PaymentSubject.COMMODITY,
            payment_mode=PaymentMode.FULL_PAYMENT
        )
    ],
    settlements=[
        Settlement(type="prepayment", amount=Money(value=1000.00, currency=Currency.RUB))
    ],
    tax_system_code=1
)
receipt = await client.receipts.create_receipt(params)

# Получение информации о чеке
receipt_info = await client.receipts.get_receipt("receipt_id")
```

### 📄 Счета (Invoices)

```python
from aioyookassa.types.params import CreateInvoiceParams

# Создание счета (используем Pydantic модель)
params = CreateInvoiceParams(
    amount=Money(value=2000.00, currency=Currency.RUB),
    description="Счет на оплату"
)
invoice = await client.invoices.create_invoice(params)

# Получение информации о счете
invoice_info = await client.invoices.get_invoice("invoice_id")
```

### 💸 Выплаты (Payouts)

```python
from aioyookassa.types.params import (
    CreatePayoutParams,
    BankCardPayoutDestinationData,
    BankCardPayoutCardData
)

# Выплата на банковскую карту
params = CreatePayoutParams(
    amount=Money(value=1000.00, currency=Currency.RUB),
    payout_destination_data=BankCardPayoutDestinationData(
        card=BankCardPayoutCardData(number="5555555555554477")
    ),
    description="Выплата по договору"
)
payout = await client.payouts.create_payout(params)

# Получение информации о выплате
payout_info = await client.payouts.get_payout("payout_id")
```

### 👤 Самозанятые (Self-Employed)

```python
from aioyookassa.types.params import (
    CreateSelfEmployedParams,
    SelfEmployedConfirmationData
)

# Создание самозанятого
params = CreateSelfEmployedParams(
    itn="123456789012",
    confirmation=SelfEmployedConfirmationData(
        type="redirect",
        confirmation_url="https://example.com/confirm"
    )
)
self_employed = await client.self_employed.create_self_employed(params)
```

### 🤝 Безопасные сделки (Deals)

```python
from aioyookassa.types.params import CreateDealParams
from aioyookassa.types.enum import FeeMoment

# Создание безопасной сделки
params = CreateDealParams(
    fee_moment=FeeMoment.PAYMENT_SUCCEEDED,
    description="Безопасная сделка"
)
deal = await client.deals.create_deal(params)

# Получение списка сделок
deals = await client.deals.get_deals()
```

### 🔔 Webhooks

#### Создание и управление webhooks

```python
from aioyookassa.types.params import CreateWebhookParams
from aioyookassa.types.enum import WebhookEvent

# Создание webhook (требует OAuth токен)
params = CreateWebhookParams(
    event=WebhookEvent.PAYMENT_SUCCEEDED,
    url="https://example.com/webhook"
)
webhook = await client.webhooks.create_webhook(
    params=params,
    oauth_token="your_oauth_token"
)

# Получение списка webhooks
webhooks = await client.webhooks.get_webhooks(oauth_token="your_oauth_token")
```

#### Обработка webhook-уведомлений

**Вариант 1: Готовый сервер (быстрый старт)**

```python
from aioyookassa.contrib.webhook_server import WebhookServer
from aioyookassa.core.webhook_handler import WebhookHandler
from aioyookassa.types.enum import WebhookEvent
from aioyookassa.types.payment import Payment

handler = WebhookHandler()

@handler.register_callback(WebhookEvent.PAYMENT_SUCCEEDED)
async def on_payment_succeeded(payment: Payment):
    print(f"✅ Платеж {payment.id} успешно выполнен")
    # Ваша бизнес-логика

server = WebhookServer(handler=handler)
server.run(host="0.0.0.0", port=8080)
```

**Вариант 2: Интеграция с существующим приложением**

```python
from aiohttp import web
from aioyookassa.core.webhook_handler import WebhookHandler
from aioyookassa.types.enum import WebhookEvent
from aioyookassa.types.payment import Payment

handler = WebhookHandler()

@handler.register_callback(WebhookEvent.PAYMENT_SUCCEEDED)
async def on_payment_succeeded(payment: Payment):
    await process_payment(payment)

async def webhook_endpoint(request):
    # Валидация IP (рекомендуется)
    if not handler.validator.is_allowed(request.remote):
        raise web.HTTPForbidden()

    # Обработка уведомления
    data = await request.json()
    notification = handler.parse_notification(data)
    await handler.handle_notification(notification)

    return web.Response(status=200)

app = web.Application()
app.router.add_post("/webhook", webhook_endpoint)
web.run_app(app)
```

**Регистрация callbacks для нескольких событий:**

```python
# Несколько событий
@handler.register_callback([
    WebhookEvent.PAYMENT_SUCCEEDED,
    WebhookEvent.PAYMENT_CANCELED
])
async def on_payment_status_change(payment: Payment):
    print(f"Payment {payment.id} status changed")

# Паттерн (все события payment.*)
@handler.register_callback("payment.*")
async def handle_all_payments(payment: Payment):
    print(f"Payment event: {payment.id}")
```

## 🔧 Контекстный менеджер

```python
from datetime import datetime
from aioyookassa.types.enum import PaymentStatus, ConfirmationType, Currency
from aioyookassa.types.params import CreatePaymentParams, GetPaymentsParams

async with YooKassa(api_key="your_key", shop_id=12345) as client:
    # Создание платежа (используем Pydantic модель)
    params = CreatePaymentParams(
        amount=Money(value=100.00, currency=Currency.RUB),
        confirmation=Confirmation(type=ConfirmationType.REDIRECT, return_url="https://example.com/return")
    )
    payment = await client.payments.create_payment(params)

    # Получение платежей за последний час (используем Pydantic модель)
    params = GetPaymentsParams(
        created_at=datetime.now(),
        status=PaymentStatus.SUCCEEDED,
        limit=5
    )
    recent_payments = await client.payments.get_payments(params)
    # Клиент автоматически закроется
```

## 🛠️ Установка и настройка

### Требования

- Python 3.8.1+
- aiohttp
- pydantic

### Установка через pip

```bash
pip install aioyookassa
```

### Установка через Poetry

```bash
poetry add aioyookassa
```

## 📖 Документация

Полная документация доступна по адресу: [aioyookassa.readthedocs.io](https://aioyookassa.readthedocs.io/en/latest/)

## 🤝 Поддержка проекта

Если библиотека оказалась полезной, вы можете поддержать проект:

- 💝 **[Tribute](https://t.me/tribute/app?startapp=dzqR)** — поддержка через Telegram
- 🐛 **Сообщить об ошибке** — [GitHub Issues](https://github.com/masasibata/aioyookassa/issues)
- 💬 **Связаться с разработчиком** — [@masaasibaata](https://t.me/masaasibaata)

## 🚀 Вклад в развитие

Мы приветствуем вклад в развитие библиотеки! Вот как вы можете помочь:

### Быстрый старт для разработчиков

```bash
# Клонирование репозитория
git clone https://github.com/masasibata/aioyookassa.git
cd aioyookassa

# Установка зависимостей для разработки
make install-dev

# Установка pre-commit хуков
make pre-commit

# Запуск всех проверок
make all-checks
```

### Доступные команды

```bash
# Тестирование
make test                 # Запуск тестов
make test-cov            # Тесты с покрытием кода
make test-fast           # Быстрые тесты без покрытия

# Качество кода
make lint                # Линтинг (Black)
make format              # Форматирование кода
make type-check          # Проверка типов (MyPy)
make all-checks          # Все проверки качества

# Сборка и публикация
make build               # Сборка пакета
make clean               # Очистка артефактов

# Документация
make docs                # Сборка документации
make docs-serve          # Локальный сервер документации

# Локальная разработка
make dev                 # Запуск пайплайна разработки локально
```

### Процесс внесения изменений

1. **Форкните репозиторий** на GitHub
2. **Создайте ветку** для ваших изменений:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Внесите изменения** и убедитесь, что все проверки проходят:
   ```bash
   make all-checks
   ```
4. **Зафиксируйте изменения**:
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```
5. **Отправьте изменения**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Создайте Pull Request** на GitHub

### Требования к Pull Request

- ✅ **Все тесты проходят** (`make test`)
- ✅ **Покрытие кода не менее 95%** (`make test-cov`)
- ✅ **Код отформатирован** (`make format`)
- ✅ **Форматирование проходит** (`make lint`)
- ✅ **Проверка типов проходит** (`make type-check`)
- ✅ **Документация обновлена** (если необходимо)
- ✅ **Описательное сообщение коммита**

### Типы вкладов

- 🐛 **Исправление багов** — исправление ошибок в коде
- ✨ **Новые функции** — добавление новой функциональности
- 📚 **Документация** — улучшение документации и примеров
- ⚡ **Оптимизация** — улучшение производительности
- 🧪 **Тесты** — добавление или улучшение тестов
- 🔧 **Инфраструктура** — улучшение инструментов разработки

### Соглашения о коммитах

Используйте [Conventional Commits](https://www.conventionalcommits.org/):

```bash
feat: add new payment method support
fix: resolve timeout issue in payment creation
docs: update API documentation
test: add tests for refund functionality
refactor: improve error handling
```

### Получение помощи

- 💬 **Вопросы** — [@masaasibaata](https://t.me/masaasibaata)
- 🐛 **Проблемы** — [GitHub Issues](https://github.com/masasibata/aioyookassa/issues)

## 📄 Лицензия

Проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

---
