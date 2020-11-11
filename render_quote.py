#! /Users/jomih/.virtualenvs/quote-web-wb0NAjhO/bin/python3
# coding: utf-8
# Author: jomih
# Version 1.0  20201109

import openpyxl

def render_quote(data):

    class cards_inventory_class:
	       #model = ''
	       #quantity = 0
           def __init__(self, model, quantity):
               self.model = model
               self.quantity = int(quantity)

    cards_inventory = []
    #el primer elemento de data es el it_number
    #lo almacenamos y lo sacamos de la lista para dejar solo el HW
    print ('data es:', data)
    it_number = data[0]
    data = data[1:]
    for item in data:
        #print ('item es:', item)
        if item=='Empty':
            continue
        found=False
        for i in range (0,len(cards_inventory)):
            if (cards_inventory[i].model == item):
                cards_inventory[i].quantity += 1
                found=True
                break
        if not(found):
            cards_inventory.append(cards_inventory_class(item,1))

    excel_reference = ''.join(['./mxquote/quotes/','reference_excel.xlsx'])
    workbook_reference = openpyxl.load_workbook(excel_reference)
    referenceSheet = workbook_reference.get_sheet_by_name('HW List')

    modelos_reference = referenceSheet['A']
    #print('modelos_reference es:', modelos_reference.value)
    descripciones_reference = referenceSheet['B']
    precios_reference = referenceSheet['C']

    excel_template = ''.join(['./mxquote/quotes/','plantilla_excel.xlsx'])
    workbook = openpyxl.load_workbook(excel_template)
    HwSheet = workbook.get_sheet_by_name('HW Quote')
    HwSheet['B2']=it_number

    start_line=4
    #add cards
    for i in range(0,len(cards_inventory)):
        HwSheet['A'+str(start_line+i)]=cards_inventory[i].model
        HwSheet['E'+str(start_line+i)]=cards_inventory[i].quantity
        #print('valor es:', cards_inventory[i].model)

        #lo siguiente no funciona, habra que hacer unos cuantos for loops
        for j in range(0,len(modelos_reference)):
            print ('cards_inventory es:', cards_inventory[i].model)
            print ('modelos_reference es:', modelos_reference[j].value)
            if (cards_inventory[i].model==modelos_reference[j].value):
                HwSheet['B'+str(start_line+i)]=descripciones_reference[j].value
                HwSheet['C'+str(start_line+i)]=precios_reference[j].value
                #print ('lo encontro')
                break

    quote_file = ''.join(['./mxquote/quotes/quote_', str(it_number), '.xlsx'])
    workbook.save(quote_file)

    #result_file = open('./result_file', 'w')
    #for item in cards_inventory:
    #    result_file.write(item.model)
    #    result_file.write('\n')
    #    result_file.write(str(item.quantity))
    #    result_file.write('\n')

    #result_file.close()

    #scb0_data = data[0]
    #scb1_data = data[1]
    #re0_data = data[2]
    #re1_data = data[3]
    #slot0_data = data[4]
    #slot1_data = data[5]
    #slot2_data = data[6]
    #slot3_data = data[7]
    #slot4_data = data[8]
    #slot5_data = data[9]

    #result_file = open('./result_file', 'w')
    #result_file.write(scb0_data)
    #result_file.write('\n')
    #result_file.write(scb1_data)
    #result_file.write('\n')
    #result_file.write(re0_data)
    #result_file.write('\n')
    #result_file.write(re1_data)
    #result_file.write('\n')
    #result_file.write(slot0_data)
    #result_file.write('\n')
    #result_file.write(slot1_data)
    #result_file.write('\n')
    #result_file.write(slot2_data)
    #result_file.write('\n')
    #result_file.write(slot3_data)
    #result_file.write('\n')
    #result_file.write(slot4_data)
    #result_file.write('\n')
    #result_file.write(slot5_data)
    #result_file.close()
    #result=[ scb0_data,re0_data,scb1_data,re1_data,slot0_data,slot1_data,slot2_data,slot3_data,slot4_data,slot5_data ]

    #return result
