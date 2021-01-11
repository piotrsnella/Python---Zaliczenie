def ile_dni_w_roku(miesiac):
    dni_w_roku = {"styczen": 31, "luty" : 28, "marzec" : 31, "kwiecien" : 30, "maj" : 31, "czerwiec" : 30, "lipiec" : 31, "siepien" : 31, "wrzesien" : 30, "pazdziernik" : 31, "listopad" : 30, "grudzien" : 31}
    return dni_w_roku[miesiac]

def pl_na_ang(month):
    pl_na_ang = {"styczen" : "january", "luty" : "February", "marzec" : "March:", "kwiecien" : "April", "maj" : "May", "czerwiec" : "June", "lipiec" : "July", "sierpien" : "september", "wrzesien" : "September", "pazdziernik" : "October", "listopad" :"November", "grudzien" : "December"}
    return pl_na_ang[month]


