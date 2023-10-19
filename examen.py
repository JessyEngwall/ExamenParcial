dia_semana = input("Dia de la semana (lunes, martes, miercoles, jueves, viernes, sabado, domingo):").lower()
hora_actual = int(input("Hora actual (en formato de 24 horas): "))
tipo_tarea = input("Tipo de tarea (estudio, deportes, descanso, trabajo): ").lower()

if 1 < hora_actual < 5:
  print("Debes estar dormido")
  
elif 5 < hora_actual <14:
  print("Debes estar en clase")

elif 14 <= hora_actual < 22:
  print("Puedes hacer tareas")


if 18 < hora_actual < 22 and tipo_tarea == "descanso": 
  print("Además de tomar una siesta puedes comezar hacer tus tareas")


if 18 < hora_actual < 22 and (dia_semana == "sabado" or dia_semana == "domingo" ): 
  print("Puedes ver una película")

elif 14 < hora_actual < 20 and dia_semana in ["lunes", "miercoles","jueves"]: 
  print("Puedes ir al gimnasio")

elif 13 < hora_actual < 15 and dia_semana in ["martes", "jueves"]: 
  print("Espero estes comiendo algo muy nutritivo")
