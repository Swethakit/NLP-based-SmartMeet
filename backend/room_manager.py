import uuid

def create_room():

    room_id = str(uuid.uuid4())[:8]

    return room_id