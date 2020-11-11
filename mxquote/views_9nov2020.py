from django.shortcuts import render

# Create your views here.
from .models import SCB, RE, MPC, Licencias, MIC, Optics, showmpc

#Pagina inicio index
def index(request):
    """
    Función vista para la página inicio del sitio.
    """

    # Renderiza la plantilla HTML index.html
    return render(
        request,
        'index.html',
    )

#pagina quote MX480/960
def quotemxh(request):
    """
    Función vista para la página de cotizacion de MX 480 o 960
    """
    results_mpc = MPC.objects.all()
    results_scb = SCB.objects.all()
    results_re = RE.objects.all()

    # Renderiza la plantilla HTML quotemxh.html con los datos en la variable contexto
    return render(
        request,
        'quotemxh.html',
        {"showmpc":results_mpc,"showscb":results_scb, "showre":results_re},
    )

#pagina result quote MX480/960
def result_quote(request):
    """
    Función vista para la página de resultado de cotizacion de MX 480
    """
    scb0_data= request.POST.get('selectscb0')
    re0_data= request.POST.get('selectre0')
    re1_data= request.POST.get('selectre1')
    scb1_data= request.POST.get('selectscb1')
    slot0_data= request.POST.get('selectslot0')
    slot1_data= request.POST.get('selectslot1')
    slot2_data= request.POST.get('selectslot2')
    slot3_data= request.POST.get('selectslot3')
    slot4_data= request.POST.get('selectslot4')
    slot5_data= request.POST.get('selectslot5')

    context= {'scb0_data':scb0_data,'re0_data':re0_data,'scb1_data':scb1_data,'re1_data':re1_data,'slot0_data':slot0_data,'slot1_data':slot1_data,'slot2_data':slot2_data,'slot3_data':slot3_data,'slot4_data':slot4_data,'slot5_data':slot5_data}

    # import script function to run
    from path_to_script import function_to_run

    # call function
    function_to_run()

    #render result
    return render(request, 'result_quote.html', context)

#pagina quote MX104
def quotemxl(request):
    """
    Función vista para la página de cotizacion de MX104
    """

    # Renderiza la plantilla HTML quotemxl.html con los datos en la variable contexto
    return render(
        request,
        'quotemxl.html',
    )

#pagina quote MPCs
def quotempc(request):
    """
    Función vista para la página de cotizacion de MPC
    """

    # Renderiza la plantilla HTML quotempc.html
    return render(
        request,
        'quotempc.html',
    )

#pagina view MPCs
def viewmpc(request):
    """
    Función vista para la página de visualizacion de MPCs
    """

    # Renderiza la plantilla HTML viewmpc.html
    return render(
        request,
        'viewmpc.html',
    )

#pagina view Licencias
def viewlicense(request):
    """
    Función vista para la página de visualizacion de Licencias
    """

    # Renderiza la plantilla HTML viewlicense.html
    return render(
        request,
        'viewlicense.html',
    )

#pagina view Opticas
def viewoptics(request):
    """
    Función vista para la página de visualizacion de Opticas
    """

    # Renderiza la plantilla HTML viewoptics.html
    return render(
        request,
        'viewoptics.html',
    )

#Para generar listas
from django.views import generic

class SCBListView(generic.ListView):
    model = SCB
    context_objetc_name = 'scb_list'

class REListView(generic.ListView):
    model = RE
    context_objetc_name = 're_list'

class MPCListView(generic.ListView):
    model = MPC
    context_object_name = 'mpc_list'
