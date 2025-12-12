Payments API
============

API для работы с платежами.

.. autoclass:: aioyookassa.core.api.payments.PaymentsAPI
   :members:
   :show-inheritance:

Методы
------

create_payment
~~~~~~~~~~~~~~

Создание нового платежа.

.. code-block:: python

    from aioyookassa.types.enum import ConfirmationType, Currency
    from aioyookassa.types.params import CreatePaymentParams
    
    params = CreatePaymentParams(
        amount=PaymentAmount(value=100.00, currency=Currency.RUB),
        confirmation=Confirmation(type=ConfirmationType.REDIRECT, return_url="https://example.com/return"),
        description="Тестовый платеж"
    )
    payment = await client.payments.create_payment(params)

Создание платежа с указанием способа оплаты
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Вы можете указать способ оплаты при создании платежа, используя параметр ``payment_method_data``:

.. code-block:: python

    from aioyookassa.types.params import (
        CreatePaymentParams,
        BankCardPaymentMethodData,
        PaymentMethodCardData,
        MobileBalancePaymentMethodData,
        SbpPaymentMethodData,
    )
    
    # Платеж банковской картой
    params = CreatePaymentParams(
        amount=PaymentAmount(value=100.00, currency=Currency.RUB),
        payment_method_data=BankCardPaymentMethodData(
            type="bank_card",
            card=PaymentMethodCardData(
                number="4111111111111111",
                expiry_year="2025",
                expiry_month="12",
                cardholder="John Doe",
                csc="123"
            )
        ),
        confirmation=Confirmation(type=ConfirmationType.REDIRECT, return_url="https://example.com/return")
    )
    payment = await client.payments.create_payment(params)
    
    # Платеж с баланса мобильного телефона
    params = CreatePaymentParams(
        amount=PaymentAmount(value=100.00, currency=Currency.RUB),
        payment_method_data=MobileBalancePaymentMethodData(
            type="mobile_balance",
            phone="79000000000"
        ),
        confirmation=Confirmation(type=ConfirmationType.REDIRECT, return_url="https://example.com/return")
    )
    payment = await client.payments.create_payment(params)
    
    # Платеж через СБП
    params = CreatePaymentParams(
        amount=PaymentAmount(value=100.00, currency=Currency.RUB),
        payment_method_data=SbpPaymentMethodData(type="sbp"),
        confirmation=Confirmation(type=ConfirmationType.REDIRECT, return_url="https://example.com/return")
    )
    payment = await client.payments.create_payment(params)

get_payments
~~~~~~~~~~~~

Получение списка платежей с возможностью фильтрации.

.. code-block:: python

    from datetime import datetime
    from aioyookassa.types.enum import PaymentStatus
    from aioyookassa.types.params import GetPaymentsParams

    params = GetPaymentsParams(
        created_at=datetime(2023, 1, 1, 12, 0, 0),
        status=PaymentStatus.SUCCEEDED,
        limit=10
    )
    payments = await client.payments.get_payments(params)

get_payment
~~~~~~~~~~~

Получение информации о конкретном платеже.

.. code-block:: python

    payment = await client.payments.get_payment("payment_id")

capture_payment
~~~~~~~~~~~~~~~

Подтверждение платежа.

.. code-block:: python

    payment = await client.payments.capture_payment("payment_id")

cancel_payment
~~~~~~~~~~~~~~

Отмена платежа.

.. code-block:: python

    payment = await client.payments.cancel_payment("payment_id")

