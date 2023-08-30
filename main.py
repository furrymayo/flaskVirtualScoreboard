from website import create_app
from flask import Flask, request, jsonify
import threading
import socket
import serial


app = create_app()

# Global variable to store the latest UDP data for each sport
udp_data = {
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
stop_udp_thread = False
stop_tcp_thread = False
stop_serial_thread = False

udp_thread = None
tcp_thread = None
serial_thread = None

# UDP Server Config
def udp_server(ip, port):
    global stop_udp_thread
    stop_udp_thread = True  # Signal the previous thread to stop

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, int(port)))

    stop_udp_thread = False  # Reset the flag

    while not stop_udp_thread:
        data, addr = sock.recvfrom(1024)
        # Your existing code to handle UDP data
        sport_code = chr(data[0])
        if sport_code == 't':  # Basketball
            udp_data['Basketball'] = parse_basketball_data(data)
        elif sport_code == 'h':  # Hockey
            udp_data['Hockey'] = parse_hockey_data(data)
        elif sport_code == 'l':  # Lacrosse
            udp_data['Lacrosse'] = parse_lacrosse_data(data)
        elif sport_code == 'f':  # Football
            udp_data['Football'] = parse_football_data(data)
        elif sport_code == 'v':  # Volleyball
            udp_data['Volleyball'] = parse_volleyball_data(data)
        elif sport_code == 'w':  # Wrestling
            udp_data['Wrestling'] = parse_wrestling_data(data)
        elif sport_code == 's':  # Soccer
            udp_data['Soccer'] = parse_soccer_data(data)
        elif sport_code == 'sft':  # Softball (unknown)
            udp_data['Softball'] = parse_softball_data(data)
        elif sport_code == 'bsb':  # Baseball (unknown)
            udp_data['Baseball'] = parse_baseball_data(data)
        # ... (other sports)

# TCP Server Config
def tcp_server(ip, port):
    global stop_tcp_thread
    stop_tcp_thread = True  # Signal the previous thread to stop

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, int(port)))

    stop_tcp_thread = False  # Reset the flag

    while not stop_tcp_thread:
        data, addr = sock.recvfrom(1024)
        # Your existing code to handle TCP data
        sport_code = chr(data[0])
        if sport_code == 't':  # Basketball
            tcp_data['Basketball'] = parse_basketball_data(data)
        elif sport_code == 'h':  # Hockey
            tcp_data['Hockey'] = parse_hockey_data(data)
        elif sport_code == 'l':  # Lacrosse
            tcp_data['Lacrosse'] = parse_lacrosse_data(data)
        elif sport_code == 'f':  # Football
            tcp_data['Football'] = parse_football_data(data)
        elif sport_code == 'v':  # Volleyball
            tcp_data['Volleyball'] = parse_volleyball_data(data)
        elif sport_code == 'w':  # Wrestling
            tcp_data['Wrestling'] = parse_wrestling_data(data)
        elif sport_code == 's':  # Soccer
            tcp_data['Soccer'] = parse_soccer_data(data)
        elif sport_code == 'sft':  # Softball (unknown)
            tcp_data['Softball'] = parse_softball_data(data)
        elif sport_code == 'bsb':  # Baseball (unknown)
            tcp_data['Baseball'] = parse_baseball_data(data)
        # ... (other sports)

# Serial Server Config
def serial_port_reader(port):
    global stop_serial_thread
    stop_serial_thread = True  # Signal the previous thread to stop

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((int(port)))

    stop_serial_thread = False  # Reset the flag

    while not stop_tcp_thread:
        data, addr = sock.recvfrom(1024)
        # Your existing code to handle TCP data
        sport_code = chr(data[0])
        if sport_code == 't':  # Basketball
            serial_data['Basketball'] = parse_basketball_data(data)
        elif sport_code == 'h':  # Hockey
            serial_data['Hockey'] = parse_hockey_data(data)
        elif sport_code == 'l':  # Lacrosse
            serial_data['Lacrosse'] = parse_lacrosse_data(data)
        elif sport_code == 'f':  # Football
            serial_data['Football'] = parse_football_data(data)
        elif sport_code == 'v':  # Volleyball
            serial_data['Volleyball'] = parse_volleyball_data(data)
        elif sport_code == 'w':  # Wrestling
            serial_data['Wrestling'] = parse_wrestling_data(data)
        elif sport_code == 's':  # Soccer
            serial_data['Soccer'] = parse_soccer_data(data)
        elif sport_code == 'sft':  # Softball (unknown)
            serial_data['Softball'] = parse_softball_data(data)
        elif sport_code == 'bsb':  # Baseball (unknown)
            serial_data['Baseball'] = parse_baseball_data(data)
        # ... (other sports)

# Parsing functions for each sport
def parse_basketball_data(data):
    pass
def parse_hockey_data(data):
    pass
def parse_lacrosse_data(data):
    pass
def parse_football_data(data):
    pass
def parse_volleyball_data(data):
    return {
        'Game Time Minute Tens': data[2],
        'Game Time Minute Ones': data[3],
        'Game Time Second Tens': data[4],
        'Game Time Second Ones': data[5],
        'Period': data[6],
        'Home Score Tens': data[7],
        'Home Score Ones': data[8],
        'Guest Score Tens': data[9],
        'Guest Score Ones': data[10],
        'Home TOL': data[11],
        'Guest TOL': data[12],
        'Home Games Won': data[18],
        'Guest Games Won': data[19],
        'Home Game 1 Score Tens': data[20],
        'Home Game 1 Score Ones': data[21],
        'Home Game 2 Score Tens': data[22],
        'Home Game 2 Score Ones': data[23],
        'Home Game 3 Score Tens': data[24],
        'Home Game 3 Score Ones': data[25],
        'Home Game 4 Score Tens': data[26],
        'Home Game 4 Score Ones': data[27],
        'Home Game 5 Score Tens': data[28],
        'Home Game 5 Score Ones': data[29],
        'Guest Game 1 Score Tens': data[30],
        'Guest Game 1 Score Ones': data[31],
        'Guest Game 2 Score Tens': data[32],
        'Guest Game 2 Score Ones': data[33],
        'Guest Game 3 Score Tens': data[34],
        'Guest Game 3 Score Ones': data[35],
        'Guest Game 4 Score Tens': data[36],
        'Guest Game 4 Score Ones': data[37],
        'Guest Game 5 Score Tens': data[38],
        'Guest Game 5 Score Ones': data[39]
    }

def parse_wrestling_data(data):
    pass
def parse_soccer_data(data):
    pass
def parse_softball_data(data):
    pass
def parse_baseball_data(data):
    pass



# Modify your update_server_config function
@app.route('/update_server_config', methods=['POST'])
def update_server_config():
    global udp_thread, stop_udp_thread, tcp_thread, stop_tcp_thread, serial_thread, stop_serial_thread

    # Stop Existing Threads
    if udp_thread is not None:
        stop_udp_thread = True  # Signal the existing thread to stop
        udp_thread.join()  # Wait for it to stop
    if tcp_thread is not None:
        stop_tcp_thread = True
        tcp_thread.join()
    if serial_thread is not None:
        stop_serial_thread = True
        serial_thread.join()

    config = request.json
    protocol = config.get('protocol', 'UDP')
    ip = config.get('ip', '0.0.0.0')
    port = config.get('port', 5005)

    if protocol == 'UDP':
        udp_thread = threading.Thread(target=udp_server, args=(ip, port))
        udp_thread.start()
    elif protocol == 'TCP':
        tcp_thread = threading.Thread(target=tcp_server, args=(ip, port))
        tcp_thread.start()
    elif protocol == 'Serial':
        serial_thread = threading.Thread(target=serial_port_reader, args=(port,))
        serial_thread.start()

    return jsonify({'status': 'Server config updated'})

@app.route('/get_raw_data/<protocol>', methods=['GET'])
def get_raw_data(protocol):
    if protocol == 'UDP':
        return jsonify(udp_data.get(sport, {})) # Fetch and return raw UDP data
    elif protocol == 'TCP':
        return jsonify(tcp_data.get(sport, {})) # Fetch and return raw TCP data
    elif protocol == 'Serial':
        return jsonify(serial_data.get(sport, {}))  # Fetch and return raw Serial data
    return "Raw data here", 200


@app.route('/get_udp_data/<sport>')
def get_udp_data(sport):
    return jsonify(udp_data.get(sport, {}))

@app.route('/get_tcp_data/<sport>')
def get_tcp_data(sport):
    return jsonify(tcp_data.get(sport, {}))

@app.route('/get_serial_data/<sport>')
def get_serial_data(sport):
    return jsonify(serial_data.get(sport, {}))

if __name__ == '__main__':
    app.run(debug=True)