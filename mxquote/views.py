from django.shortcuts import render

# Create your views here.
from .models import SCB, RE, MPC, Licencias, MIC, Optics, showmpc, showscb, showre, showmic, showlicense

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

#pagina quote MX480
def quotemxh(request):
    """
    Función vista para la página de cotizacion de MX 480
    """
    results_mpc = MPC.objects.all()
    results_scb = SCB.objects.all()
    results_re = RE.objects.all()
    results_mic = MIC.objects.all()
    results_license = Licencias.objects.all()

    # Renderiza la plantilla HTML quotemxh.html con los datos en la variable contexto
    return render(
        request,
        'quotemxh.html',
        {"showmpc":results_mpc,"showscb":results_scb, "showre":results_re, "showmic":results_mic, "showlicense":results_license},
    )

#pagina quote MX960
def quotemx960(request):
    """
    Función vista para la página de cotizacion de MX960
    """
    results_mpc = MPC.objects.all()
    results_scb = SCB.objects.all()
    results_re = RE.objects.all()
    results_mic = MIC.objects.all()
    results_license = Licencias.objects.all()

    # Renderiza la plantilla HTML quotemxh.html con los datos en la variable contexto
    return render(
        request,
        'quotemx960.html',
        {"showmpc":results_mpc,"showscb":results_scb, "showre":results_re, "showmic":results_mic, "showlicense":results_license},
    )

#pagina make quote MX480/960
def make_quote(request):
    """
    Función vista para la página de creación de cotizacion de MX480
    """
    it_data = request.POST.get('it_number')
    chasis_data = request.POST.get('selectchasis')
    scb0_data = request.POST.get('selectscb0')
    if not(scb0_data):
        scb0_data='Empty'
    re0_data = request.POST.get('selectre0')
    if not(re0_data):
        re0_data='Empty'
    scb1_data = request.POST.get('selectscb1')
    if not(scb1_data):
        scb1_data='Empty'
    re1_data = request.POST.get('selectre1')
    if not(re1_data):
        re1_data='Empty'

    slot0_data = request.POST.get('selectslot0')
    if not(slot0_data):
        slot0_data='Empty'
    slot0mic0_data = request.POST.get('selectslot0mic0')
    if not(slot0mic0_data):
        slot0mic0_data='Empty'
    slot0mic1_data = request.POST.get('selectslot0mic1')
    if not(slot0mic1_data):
        slot0mic1_data='Empty'

    slot1_data = request.POST.get('selectslot1')
    if not(slot1_data):
        slot1_data='Empty'
    slot1mic0_data = request.POST.get('selectslot1mic0')
    if not(slot1mic0_data):
        slot1mic0_data='Empty'
    slot1mic1_data = request.POST.get('selectslot1mic1')
    if not(slot1mic1_data):
        slot1mic1_data='Empty'

    slot2_data = request.POST.get('selectslot2')
    if not(slot2_data):
        slot2_data='Empty'
    slot2mic0_data = request.POST.get('selectslot2mic0')
    if not(slot2mic0_data):
        slot2mic0_data='Empty'
    slot2mic1_data = request.POST.get('selectslot2mic1')
    if not(slot2mic1_data):
        slot2mic1_data='Empty'

    slot3_data = request.POST.get('selectslot3')
    if not(slot3_data):
        slot3_data='Empty'
    slot3mic0_data = request.POST.get('selectslot3mic0')
    if not(slot3mic0_data):
        slot3mic0_data='Empty'
    slot3mic1_data = request.POST.get('selectslot3mic1')
    if not(slot3mic1_data):
        slot3mic1_data='Empty'

    slot4_data = request.POST.get('selectslot4')
    if not(slot4_data):
        slot4_data='Empty'
    slot4mic0_data = request.POST.get('selectslot4mic0')
    if not(slot4mic0_data):
        slot4mic0_data='Empty'
    slot4mic1_data = request.POST.get('selectslot4mic1')
    if not(slot4mic1_data):
        slot4mic1_data='Empty'

    slot5_data = request.POST.get('selectslot5')
    if not(slot5_data):
        slot5_data='Empty'
    slot5mic0_data = request.POST.get('selectslot5mic0')
    if not(slot5mic0_data):
        slot5mic0_data='Empty'
    slot5mic1_data = request.POST.get('selectslot5mic1')
    if not(slot5mic1_data):
        slot5mic1_data='Empty'

    #context= {'scb0_data':scb0_data,'re0_data':re0_data,'scb1_data':scb1_data,'re1_data':re1_data,'slot0_data':slot0_data,'slot1_data':slot1_data,'slot2_data':slot2_data,'slot3_data':slot3_data,'slot4_data':slot4_data,'slot5_data':slot5_data}
    context = [it_data, chasis_data, scb0_data, scb0_data, re0_data, re1_data, slot0_data, slot1_data, slot2_data, slot3_data, slot4_data, slot5_data, slot0mic0_data, slot0mic1_data, slot1mic0_data, slot1mic1_data, slot2mic0_data, slot2mic1_data, slot3mic0_data, slot3mic1_data, slot4mic0_data, slot4mic1_data, slot5mic0_data, slot5mic1_data ]

    # import script function to run
    from render_quote import render_quote

    # call function
    render_quote(context)

    #render result
    return render(
        request,
        'result_quote.html',
    )

#pagina result_quote MX480
def result_quote(request):
    """
    Función vista para resultado quote de MX480
    """
    # Renderiza la plantilla HTML quotemxl.html con los datos en la variable contexto
    return render(
        request,
        'result_quote.html',
    )

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
    Función vista para la página de cotizacion de MPC y MICs
    """

    # Renderiza la plantilla HTML quotempc.html
    return render(
        request,
        'quotempc.html',
    )

#pagina view MPCs
#def viewmpc(request):
#    """
#    Función vista para la página de visualizacion de MPCs
#    """

#    # Renderiza la plantilla HTML viewmpc.html
#    return render(
#        request,
#        'viewmpc.html',
#    )

#def viewsbc(request):
#    """
#    Función vista para la página de visualizacion de SBCs
#    """

#    # Renderiza la plantilla HTML viewmpc.html
#    return render(
#        request,
#        'viewsbc.html',
#    )

#pagina view Licencias
#    """
#    Función vista para la página de visualizacion de Licencias
#    """

#    # Renderiza la plantilla HTML viewlicense.html
#    return render(
#        request,
#        'viewlicense.html',
#    )

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

#pagina view Opticas
#def viewmic(request):
#    """
#    Función vista para la página de visualizacion de MICs
#    """

#    # Renderiza la plantilla HTML viewoptics.html
#    return render(
#        request,
#        'viewmic.html',
#    )

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

class MICListView(generic.ListView):
    model = MIC
    context_object_name = 'mic_list'

class LicenseListView(generic.ListView):
    model = Licencias
    context_object_name = 'license_list'
