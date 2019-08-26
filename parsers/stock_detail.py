from bs4 import BeautifulSoup
def retireve_bse_nse_data(div_soup):
    dict = {}
    bsestock = find_val(div_soup, 'div', 'id', 'content_full')
    print(f"The bsestock is {bsestock}")
    content_base= find_val(bsestock, 'div', 'id', 'content_bse')
    print(f"The content bse is {content_base}")
    bsetick = find_val(content_base, 'div', 'id', 'Bse_Prc_tick_div')
    bsetick_span = find_val(bsetick, 'span', 'id', 'Bse_Prc_tick')
    print(f"the value is {bsetick.text}")
    dict['bse']['price'] = bsetick.text 
    return dict    

def find_val(html, element, type, value):
    soup = BeautifulSoup(html.text, "html5lib")
    str = ""
    if(type == 'class'):
        str = soup.find(element, class_ = value)
    elif(type == 'id'):
        str = soup.find(element, id= value)
    return str
