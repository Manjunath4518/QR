from django.shortcuts import render
from .forms import *
import qrcode
import os
from django.conf import settings

def genrate_qr_code(request):
    if request.method == 'POST':
        form = QRcodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['rest_name']
            url = form.cleaned_data['url']
            
            #Gen QR
            qr = qrcode.make(url)
            file_name = res_name.replace(" ","_")+'_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT,file_name)
            qr.save(file_path)
            qr_url = os.path.join(settings.MEDIA_URL,file_name)
            context = {
                'res':res_name,
                'qr_url':qr_url,
                'file_name':file_name,
            }
            return render(request,'qr_result.html',context)
            
    else:
        form = QRcodeForm()
        context = {
            'form':form
        }
        return render(request,'genrate_qr_code.html',context)