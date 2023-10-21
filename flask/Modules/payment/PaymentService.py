# -*- coding: utf-8 -*-

import importlib.util
from datetime import datetime
class PaymentService:
    def __init__(self):
        spec = importlib.util.spec_from_file_location(
            "ecpay_payment_sdk",
            "./Modules/payment/ecpay_payment_sdk.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)


    def Accountdeposit(self,user_id,amount,account,customername):
        spec = importlib.util.spec_from_file_location(
            "ecpay_payment_sdk",
            "./Modules/payment/ecpay_payment_sdk.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        order_params = {
            'MerchantTradeNo': datetime.now().strftime("NO%Y%m%d%H%M%S"),
            'StoreID': '',
            'MerchantTradeDate': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'PaymentType': 'aio',
            'TotalAmount': amount,
            'TradeDesc': '訂單測試',
            'ItemName': '商品1#商品2',
            'ReturnURL': ' https://8a52-122-118-21-87.ngrok-free.app/api/account/receive_result',
            'ChoosePayment': 'ALL',
            'ClientBackURL': 'https://www.ecpay.com.tw/client_back_url.php',
            'ItemURL': 'https://www.ecpay.com.tw/item_url.php',
            'Remark': '交易備註',
            'ChooseSubPayment': '',
            'OrderResultURL': 'https://www.ecpay.com.tw/order_result_url.php',
            'NeedExtraPaidInfo': 'Y',
            'DeviceSource': '',
            'IgnorePayment': '',
            'PlatformID': '',
            'InvoiceMark': 'N',
            'CustomField1': str(user_id),
            'CustomField2': str(customername),
            'CustomField3': str(account),
            'CustomField4': 'testpay',
            'EncryptType': 1,
        }

        extend_params_1 = {
            'ExpireDate': 7,
            'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',
            'ClientRedirectURL': '',
        }

        extend_params_2 = {
            'StoreExpireDate': 15,
            'Desc_1': '',
            'Desc_2': '',
            'Desc_3': '',
            'Desc_4': '',
            'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',
            'ClientRedirectURL': '',
        }

        extend_params_3 = {
            'BindingCard': 0,
            'MerchantMemberID': '',
        }

        extend_params_4 = {
            'Redeem': 'N',
            'UnionPay': 0,
        }

        inv_params = {
            # 'RelateNumber': 'Tea0001', # 特店自訂編號
            'CustomerID': str(user_id), # 客戶編號
            # 'CustomerIdentifier': '53348111', # 統一編號
            'CustomerName': str(customername),
            'CustomerAddr': str(account),
            # 'CustomerPhone': '0912345678', # 客戶手機號碼
            # 'CustomerEmail': 'abc@ecpay.com.tw',
            # 'ClearanceMark': '2', # 通關方式
            # 'TaxType': '1', # 課稅類別
            # 'CarruerType': '', # 載具類別
            # 'CarruerNum': '', # 載具編號
            # 'Donation': '1', # 捐贈註記
            # 'LoveCode': '168001', # 捐贈碼
            # 'Print': '1',
            # 'InvoiceItemName': '測試商品1|測試商品2',
            # 'InvoiceItemCount': '2|3',
            # 'InvoiceItemWord': '個|包',
            # 'InvoiceItemPrice': '35|10',
            # 'InvoiceItemTaxType': '1|1',
            # 'InvoiceRemark': '測試商品1的說明|測試商品2的說明',
            # 'DelayDay': '0', # 延遲天數
            # 'InvType': '07', # 字軌類別
        }

    # 建立實體
        ecpay_payment_sdk = module.ECPayPaymentSdk(
            MerchantID='3002607',
            HashKey='pwFHCqoQZGmho4w6',
            HashIV='EkRm7iFT261dpevs'
        )

        # 合併延伸參數
        order_params.update(extend_params_1)
        order_params.update(extend_params_2)
        order_params.update(extend_params_3)
        order_params.update(extend_params_4)

    # 合併發票參數
        order_params.update(inv_params)

        try:
            # 產生綠界訂單所需參數
            final_order_params = ecpay_payment_sdk.create_order(order_params)

            # 產生 html 的 form 格式
            action_url = 'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5'  # 測試環境
            # action_url = 'https://payment.ecpay.com.tw/Cashier/AioCheckOut/V5' # 正式環境
            html = ecpay_payment_sdk.gen_html_post_form(action_url, final_order_params)
            # print(html)
            # print("--1--")
            return html
        except Exception as error:
            return print(error)
