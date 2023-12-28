from pypresence import Presence
import time

def update_presence():
    client_id = 'เติม APPLICATION ID'
    RPC = Presence(client_id)
    RPC.connect()

    try:
        while True:
            current_time = int(time.time())
            
            discord_presence = {
                'state': '[New-Species]',
                'details': 'Template Dino Master',
                'large_image': 'photoshoplogo',
                'large_text': 'Photoshop',
                'small_text': 'SP - Level 1',
                'party_id': 'ae488379-351d-4a4f-ad32-2b9b01c91657',
                'party_size': [2, 6], 
            }

            RPC.update(**discord_presence)
            
            time.sleep(15)
    except KeyboardInterrupt:

        RPC.close()

if __name__ == '__main__':
    update_presence()
