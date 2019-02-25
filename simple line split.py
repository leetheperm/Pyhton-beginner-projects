import re
data = ('''Bushy Green 
Greenwich 
Hyde 
Kensington 
Regent's 
Richmond 
St James's
Alexandra 
Arnos 
Barking 
Barra Hall 
Battersea 
Blackheath 
Brockwell 
Burgess 
Clissold 
Crystal Palace 
Dulwich 
Enfield Town 
Finsbury 
Forster Memorial 
Hampstead Heath 
Hanworth 
Holland 
Mayesbrook 
Mountsfield 
Old Deer 
Parsloes 
Primrose Hill 
Pymmes 
Queen's Park 
Queen Elizabeth Olympic Park 
Ravenscourt 
Ruskin 
Southwark 
Valentines 
Victoria 
Wandsworth 
Wanstead 
West Ham 
Wimbledon	
Aveley 
Crayford 
Erith 
Hackney 
Hornchurch 
Ickenham 
Ingrebourne 
Leyton 
Rainham 
Tottenham 
Walthamstow
 Wennington 
Woodberry Wetlands  
Bostall Braeburn 
Coldfall Copse 
Dulwich 
Epping Forest 
Grangewood Park 
Highgate 
Lesnes Abbey 
Mad Bess 
Old Park 
Oxleas Park 
Petts 
Queen's 
Russia Dock 
Sydenham Hill
Belair Park 
Boston Manor Park 
Broomfield House 
Cannizaro Park 
Chiswick House 
Danson Park 
Grovelands Park 
Grove Park 
Gunnersbury Park 
Hall Place 
Hampton Court Park 
Hillingdon Court 
Kenwood House 
Lamorbey Park 
Langtons Manor House Gardens 
Marble Hill Park 
Morden Hall Park 
Morden Park 
Osterley Park 
Syon House 
Valence House Museum 
Walpole Park
Kew Gardens 
London Wetland Centre	
Phoenix Garden''')

split_data = [data.splitlines()]
print(split_data)