from ast import parse
from website import create_app
from flask import Flask, request, jsonify
import threading
import socket
import serial
import serial.tools.list_ports


app = create_app()

# Global variable to store the latest UDP data for each sport
parsed_data = {
    'Basketball': {},
    'Hockey': {},
    'Lacrosse': {},
    'Football': {},
    'Volleyball': {},
    'Wrestling': {},
    'Track': {},
    'Soccer': {},
    'Softball': {},
    'Baseball': {},
}

# Add a flag to signal the thread to stop
stop_serial_thread = False
serial_thread = None

# Serial Server Config
def serial_port_reader(port):
    global stop_serial_thread, parsed_data # Added parsed_data to global
    stop_serial_thread = True  # Signal the previous thread to stop

    ser = serial.Serial(port, 9600) # Initialize serial Port

    stop_serial_thread = False # Reset the flag

    while not stop_serial_thread:
        data = ser.readline().decode('ascii').strip()  # Read ASCII coded decimal data
        print(f"Received Serial Data: {data}")  # Debugging Line
        
        if len(data) == 0 or data[0] not in ['t', 'h', 'l', 'f', 'v', 'w', 's', 'sft', 'bsb']:
            print("Error: Invalid or missing sport code in received data.")
            continue  # Skip the rest of the loop and wait for the next data

        # Your existing code to handle Serial data
        sport_code = data[0]    # sport code read. Might be data[1] based on document?
        if sport_code == 't':  # Basketball
            parsed_data['Basketball'] = parse_basketball_data_ascii(data)
        elif sport_code == 'h':  # Hockey
            parsed_data['Hockey'] = parse_hockey_data_ascii(data)
        elif sport_code == 'l':  # Lacrosse
            parsed_data['Lacrosse'] = parse_lacrosse_data_ascii(data)
        elif sport_code == 'f':  # Football
            parsed_data['Football'] = parse_football_data_ascii(data)
        elif sport_code == 'v':  # Volleyball
            parsed_data['Volleyball'] = parse_volleyball_data_ascii(data)
        elif sport_code == 'w':  # Wrestling
            parsed_data['Wrestling'] = parse_wrestling_data_ascii(data)
        elif sport_code == 's':  # Soccer
            parsed_data['Soccer'] = parse_soccer_data_ascii(data)
        elif sport_code == 'sft':  # Softball (unknown)
            parsed_data['Softball'] = parse_softball_data_ascii(data)
        elif sport_code == 'bsb':  # Baseball (unknown)
            parsed_data['Baseball'] = parse_baseball_data_ascii(data)
        # ... (other sports)

# Parsing functions for each sport
def parse_basketball_data_ascii(data):
    pass
def parse_hockey_data_ascii(data):
    pass
def parse_lacrosse_data_ascii(data):
    pass
def parse_football_data_ascii(data):
    pass
def parse_volleyball_data_ascii(data):
    try:
        # Convert ASCII Coded Decimal to appropriate Data Types
        return {
            'Game Time Minute Tens': int(data[1]),
            'Game Time Minute Ones': int(data[2]),
            'Game Time Second Tens': int(data[3]),
            'Game Time Second Ones': int(data[4]),
            'Period': int(data[5]),
            'Home Score Tens': int(data[6]),
            'Home Score Ones': int(data[7]),
            'Guest Score Tens': int(data[8]),
            'Guest Score Ones': int(data[9]),
            'Home TOL': int(data[10]),
            'Guest TOL': int(data[11]),
            'Home Games Won': int(data[19]),
            'Guest Games Won': int(data[18]),
            'Home Game 1 Score Tens': int(data[19]),
            'Home Game 1 Score Ones': int(data[20]),
            'Home Game 2 Score Tens': int(data[21]),
            'Home Game 2 Score Ones': int(data[22]),
            'Home Game 3 Score Tens': int(data[23]),
            'Home Game 3 Score Ones': int(data[24]),
            'Home Game 4 Score Tens': int(data[25]),
            'Home Game 4 Score Ones': int(data[26]),
            'Home Game 5 Score Tens': int(data[27]),
            'Home Game 5 Score Ones': int(data[28]),
            'Guest Game 1 Score Tens': int(data[29]),
            'Guest Game 1 Score Ones': int(data[30]),
            'Guest Game 2 Score Tens': int(data[31]),
            'Guest Game 2 Score Ones': int(data[32]),
            'Guest Game 3 Score Tens': int(data[33]),
            'Guest Game 3 Score Ones': int(data[34]),
            'Guest Game 4 Score Tens': int(data[35]),
            'Guest Game 4 Score Ones': int(data[36]),
            'Guest Game 5 Score Tens': int(data[37]),
            'Guest Game 5 Score Ones': int(data[38])
        }
    except Exception as e:
        return {'error': f'Data Format Mismatch: {str(e)}'}

def parse_wrestling_data_ascii(data):
    pass
def parse_soccer_data_ascii(data):
    pass
def parse_softball_data_ascii(data):
    pass
def parse_baseball_data_ascii(data):
    pass



# Modify your update_server_config function
@app.route('/update_server_config', methods=['POST'])
def update_server_config():
    global serial_thread, stop_serial_thread

    # Stop Existing Threads
    if serial_thread is not None:
        stop_serial_thread = True
        serial_thread.join()

    config = request.json
    port = config.get('port', 'COM1')

    serial_thread = threading.Thread(target=serial_port_reader, args=(port,))
    serial_thread.start()

    return jsonify({'status': 'Server config updated'})

@app.route('/get_raw_data/<sport>', methods=['GET'])
def get_raw_data(sport):
    return jsonify(parsed_data.get(sport, {}))

if __name__ == '__main__':
    app.run(debug=True)