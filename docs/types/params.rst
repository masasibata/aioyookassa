Payment Method Data Types
==========================

Типы данных для указания способа оплаты при создании платежа.

PaymentMethodData
-----------------

Union тип, объединяющий все возможные способы оплаты.

.. autoclass:: aioyookassa.types.params.PaymentMethodData
   :members:
   :show-inheritance:

Способы оплаты
--------------

SberLoanPaymentMethodData
~~~~~~~~~~~~~~~~~~~~~~~~~~

Способ оплаты "Сбербанк в рассрочку".

.. autoclass:: aioyookassa.types.params.SberLoanPaymentMethodData
   :members:
   :show-inheritance:

MobileBalancePaymentMethodData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Способ оплаты с баланса мобильного телефона.

.. autoclass:: aioyookassa.types.params.MobileBalancePaymentMethodData
   :members:
   :show-inheritance:

BankCardPaymentMethodData
~~~~~~~~~~~~~~~~~~~~~~~~~~

Способ оплаты банковской картой.

.. autoclass:: aioyookassa.types.params.BankCardPaymentMethodData
   :members:
   :show-inheritance:

CashPaymentMethodData
~~~~~~~~~~~~~~~~~~~~~

Способ оплаты наличными.

.. autoclass:: aioyookassa.types.params.CashPaymentMethodData
   :members:
   :show-inheritance:

SberBnplPaymentMethodData
~~~~~~~~~~~~~~~~~~~~~~~~~~

Способ оплаты "Плати частями" от Сбербанка.

.. autoclass:: aioyookassa.types.params.SberBnplPaymentMethodData
   :members:
   :show-inheritance:

SbpPaymentMethodData
~~~~~~~~~~~~~~~~~~~~~

Способ оплаты через Систему быстрых платежей (СБП).

.. autoclass:: aioyookassa.types.params.SbpPaymentMethodData
   :members:
   :show-inheritance:

B2BSberbankPaymentMethodData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Способ оплаты B2B Сбербанк.

.. autoclass:: aioyookassa.types.params.B2BSberbankPaymentMethodData
   :members:
   :show-inheritance:

ElectronicCertificatePaymentMethodData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Способ оплаты электронным сертификатом.

.. autoclass:: aioyookassa.types.params.ElectronicCertificatePaymentMethodData
   :members:
   :show-inheritance:

YooMoneyPaymentMethodData
~~~~~~~~~~~~~~~~~~~~~~~~~~

Способ оплаты через YooMoney.

.. autoclass:: aioyookassa.types.params.YooMoneyPaymentMethodData
   :members:
   :show-inheritance:

SberbankPaymentMethodData
~~~~~~~~~~~~~~~~~~~~~~~~~~

Способ оплаты через Сбербанк Онлайн.

.. autoclass:: aioyookassa.types.params.SberbankPaymentMethodData
   :members:
   :show-inheritance:

TinkoffBankPaymentMethodData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Способ оплаты через Тинькофф Банк.

.. autoclass:: aioyookassa.types.params.TinkoffBankPaymentMethodData
   :members:
   :show-inheritance:

Вспомогательные типы
--------------------

PaymentMethodCardData
~~~~~~~~~~~~~~~~~~~~~

Данные банковской карты для способов оплаты.

.. autoclass:: aioyookassa.types.params.PaymentMethodCardData
   :members:
   :show-inheritance:

ElectronicCertificateArticle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Статья для электронного сертификата.

.. autoclass:: aioyookassa.types.params.ElectronicCertificateArticle
   :members:
   :show-inheritance:

ElectronicCertificateData
~~~~~~~~~~~~~~~~~~~~~~~~~~

Данные электронного сертификата от ФЭС НСПК.

.. autoclass:: aioyookassa.types.params.ElectronicCertificateData
   :members:
   :show-inheritance:

Примеры использования
---------------------

Банковская карта
~~~~~~~~~~~~~~~~

.. code-block:: python

    from aioyookassa.types.params import (
        BankCardPaymentMethodData,
        PaymentMethodCardData,
    )
    
    payment_method_data = BankCardPaymentMethodData(
        type="bank_card",
        card=PaymentMethodCardData(
            number="4111111111111111",
            expiry_year="2025",
            expiry_month="12",
            cardholder="John Doe",
            csc="123"
        )
    )

Мобильный баланс
~~~~~~~~~~~~~~~~

.. code-block:: python

    from aioyookassa.types.params import MobileBalancePaymentMethodData
    
    payment_method_data = MobileBalancePaymentMethodData(
        type="mobile_balance",
        phone="79000000000"
    )

СБП
~~~

.. code-block:: python

    from aioyookassa.types.params import SbpPaymentMethodData
    
    payment_method_data = SbpPaymentMethodData(type="sbp")

B2B Сбербанк
~~~~~~~~~~~~

.. code-block:: python

    from aioyookassa.types.params import B2BSberbankPaymentMethodData
    from aioyookassa.types.payment import VatData, PaymentAmount
    
    payment_method_data = B2BSberbankPaymentMethodData(
        type="b2b_sberbank",
        payment_purpose="Оплата по договору №123",
        vat_data=VatData(
            type="calculated",
            amount=PaymentAmount(value="100.00", currency="RUB"),
            rate="20"
        )
    )

Электронный сертификат
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from aioyookassa.types.params import (
        ElectronicCertificatePaymentMethodData,
        ElectronicCertificateArticle,
        ElectronicCertificateData,
        PaymentAmount,
    )
    
    payment_method_data = ElectronicCertificatePaymentMethodData(
        type="electronic_certificate",
        articles=[
            ElectronicCertificateArticle(
                article_number=1,
                tru_code="329921120.06001010200080001643",
                article_name="Товар",
                quantity=1,
                price=PaymentAmount(value="100.00", currency="RUB")
            )
        ],
        electronic_certificate=ElectronicCertificateData(
            amount=PaymentAmount(value="100.00", currency="RUB"),
            basket_id="basket_123"
        )
    )


