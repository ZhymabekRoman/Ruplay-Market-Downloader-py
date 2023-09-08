import requests
import uuid


def get_app_info(application_id: str) -> dict:
    headers = {
        'Authorization': 'Bearer',
        'rumarket-api': 'Bearer',
        'User-Agent': f'RuMarket(3.4.1);WayDroid x86 Device Waydroid;30;{uuid.uuid4().hex};',
        'Accept': 'application/json',
        'Accept-Charset': 'UTF-8',
        'Host': 'store-api.ruplay.market',
        'Connection': 'Keep-Alive',
    }

    response = requests.get(f'https://store-api.ruplay.market/api/v1/app/getApp/{application_id}', headers=headers)
    return response.json()


def download_app(application_id: str) -> None:
    app_info = get_app_info(application_id)

    application_donwload_id = app_info['data']['latestApk']['name']

    headers = {
        'rumarket-api': 'Bearer',
        'User-Agent': 'AndroidDownloadManager/11 (Linux; U; Android 11; WayDroid x86 Device Build/RQ3A.211001.001)',
        'Connection': 'close',
        'Host': 'cdn.ruplay.market',
    }

    response = requests.get(f'https://cdn.ruplay.market/data/apks/{application_donwload_id}', headers=headers)

    print("Downloading, please wait....")

    with open(f'{application_id}.apk', 'wb') as f:
        f.write(response.content)


def main():
    application_id = input("Enter application id (like - ru.dublgis.dgismobile): ")
    download_app(application_id)


main()
