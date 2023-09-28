from django.shortcuts import render
import requests
from django.conf import settings

def mastercard_currency_converter(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        from_currency = request.POST['from_currency']
        to_currency = request.POST['to_currency']

        # Make API call to Mastercard API for currency conversion
        response = requests.get(
            f'https://sandbox.api.mastercard.com/...?...&Amount={amount}&FromCurrency={from_currency}&ToCurrency={to_currency}',
            auth=(settings.MASTERCARD_CONSUMER_KEY, settings.MASTERCARD_KEY_ALIAS)
        )

        if response.status_code == 200:
            conversion_result = response.json()
            converted_amount = conversion_result['convertedAmount']
            return render(request, 'result.html', {'converted_amount': converted_amount})
        else:
            return render(request, 'error.html')

    return render(request, 'converter.html')
