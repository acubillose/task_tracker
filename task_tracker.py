import sys
import json
import os
from datetime import datetime

# Archivo donde guardaremos las tareas
TASKS_FILE = "tasks.json"

# Cargamos el archivo JSON si existe, sino, creamos una lista vacía
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "w") as file:
        json.dump([], file)
        
# Función para cargar tareas desde el archivo
def load_tasks():
    with open(TASKS_FILE, "r") as file:
        return json.load(file)
    
# Función para guardar tareas en el archivo
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
        
# Función para agregar una nueva tarea
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarea agregada: {new_task['id']} - {new_task['description']}")
    
# Función para listar tareas
def list_tasks(status=None):
    tasks = load_tasks()
    
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    
    if tasks:
        for task in tasks:
            print(f"{task['id']}. {task['description']} - {task['status']}")
    else:
        print("No hay tareas para mostrar.")
        
# Función para actualizar el estado de una tarea
def update_task_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Tarea {task_id} marcada como {status}.")
            return
    print(f"No se encontró la tarea con ID {task_id}.")
    
# Funcion para eliminar tarea
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Tarea {task_id} eliminada.")
    
# Funcion para actualizar descripción de una tarea
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Tarea {task_id} actualizada.")
            return
    print(f"No se encontró la tarea con ID {task_id}.")
        
# Función principal para manejar los comandos
def main():
    if len(sys.argv) < 2:
        print("Uso: task-cli [comando] [argumentos]")
        sys.exit(1)
    
    command = sys.argv[1]

    if command == "add":
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    elif command == "mark-in-progress":
        task_id = int(sys.argv[2])
        update_task_status(task_id, "in-progress")
    elif command == "mark-done":
        task_id = int(sys.argv[2])
        update_task_status(task_id, "done")
    elif command == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif command == "update":
        task_id = int(sys.argv[2])
        new_description = " ".join(sys.argv[3:])
        update_task(task_id, new_description)
    else:
        print("Comando no reconocido")
        
if __name__ == "__main__":
    main()