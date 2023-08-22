import heapq

data = [
            {"company":"apple","price":"1300"},
            {"company":"google","price":"1700"},
            {"company":"microsoft","price":"1500"},
            {"company":"facebook","price":"1300"},
            {"company":"twitter","price":"2000"},
            {"company":"linkedin","price":"1200"}
        ]


print(heapq.nsmallest(2, data, key=lambda stock: stock["price"]))