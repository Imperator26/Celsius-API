# Copyright (C) 2019 Federico A. Corazza - All Rights Reserved
# You may use, distribute and modify this code under the
# terms described in the LICENSE document at the root of
# this project.

import json

import requests

from .utils import load_api_key, handle_response

api_key_path = "api.key"
endpoint = "https://wallet-api.staging.celsius.network"
headers = {
    "accept": "application/json",
    "X-Cel-User-Token": load_api_key(api_key_path)
}


# Health

@handle_response
def echo(message, method="GET"):
    if method == "GET":
        return requests.get(
            f"{endpoint}/wallet/echo/{message}",
            headers=headers
        )
    else:
        payload = {
            "message": message
        }

        return requests.post(
            f"{endpoint}/wallet/echo",
            headers=headers,
            data=json.dumps(payload)
        )


# Wallet

@handle_response
def balance(coin=None):
    if coin:
        return requests.get(
            f"{endpoint}/wallet/{coin}/balance",
            headers=headers
        )
    else:
        return requests.get(
            f"{endpoint}/wallet/balance",
            headers=headers
        )


@handle_response
def transactions(coin=None, page=0, per_page=10):
    params = {
        "page": page,
        "per_page": per_page
        }

    if coin:
        return requests.get(
            f"{endpoint}/wallet/{coin}/transactions",
            headers=headers,
            params=params
        )
    else:
        return requests.get(
            f"{endpoint}/wallet/transactions",
            headers=headers,
            params=params
        )


@handle_response
def interest():
    return requests.get(
        f"{endpoint}/wallet/interest",
        headers=headers
    )


@handle_response
def deposit(coin):
    return requests.get(
        f"{endpoint}/wallet/{coin}/deposit",
        headers=headers
    )


@handle_response
def withdraw(coin, address, amount):
    payload = {
        "address": address,
        "amount": amount
    }

    return requests.post(
        f"{endpoint}/wallet/{coin}/withdraw",
        headers=headers,
        data=json.dumps(payload)
    )


@handle_response
def transaction_status(transaction):
    return requests.get(
        f"{endpoint}/transactions/{transaction}/status",
        headers=headers
    )


# KYC

@handle_response
def kyc_status():
    return requests.get(
        f"{endpoint}/kyc",
        headers=headers
    )


@handle_response
def kyc_verify(payload):
    return requests.post(
        f"{endpoint}/kyc",
        headers=headers,
        data=json.dumps(payload)
    )


# Utils

@handle_response
def supported_currencies():
    return requests.get(
        f"{endpoint}/util/supported_currencies",
        headers=headers
    )


@handle_response
def interest_rates():
    return requests.get(
        f"{endpoint}/util/interest/rates",
        headers=headers
    )


@handle_response
def statistics():
    return requests.get(
        f"{endpoint}/util/statistics",
        headers=headers
    )


# Institutional

@handle_response
def institutional_users():
    return requests.post(
        f"{endpoint}/institutional/users",
        headers=headers
    )


@handle_response
def institutional_metadata(id):
    return requests.post(
        f"{endpoint}/institutional/{id}/metadata",
        headers=headers
    )


@handle_response
def institutional_withdrawal_address(id):
    return requests.post(
        f"{endpoint}/institutional/{id}/withdrawal-address",
        headers=headers
    )


@handle_response
def institutional_user(payload):
    return requests.post(
        f"{endpoint}/institutional/user",
        headers=headers,
        data=json.dumps(payload)
    )
