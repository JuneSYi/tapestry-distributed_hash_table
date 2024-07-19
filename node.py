import asyncio
import hashlib
import random

class Node:
    def __init__(self, port=9999):
        self.node_id = ""
        self.routing_table= {} # neighbor map
        self.port = port
        self.dolr_store = {}
        self.db_path = ""

    def new(self, port: int, db_path: str):
        self.port = port
        self.db_path = db_path
        # unique 160-bit hash represented by 40-character string hex
        self.node_id = hashlib.sha1(str(random.random()).encode()).hexdigest()
        self.build_routing_table(self.node_id)

    async def discover_nodes(self, router_ip, receiver_port):
        ''' finds and connects to other nodes in the network
        Assumption: other nodes have a discovery protocol that's broadcasted from their device
        '''
        loop = asyncio.get_running_loop()
        transport, protocol = await loop.create_datagram_endpoint(
                lambda: self.findNodeProtocol(),
                local_addr=(router_ip, receiver_port)
            )
        try:
            while True:
                await asyncio.sleep(10)
        except KeyboardInterrupt:
            await transport.stop()

    # add helper functions
    def findNodeProtocol(self):
        ''' function receive messages
        decode message using encryption protocol
        runs self.send_verification()
        '''
        pass

    def send_verification(self):
        '''
        sends encryption verification request to found node
        runs self.verification_response()
        '''
    def verification_response(self):

    def build_routing_table(self, node_id):
        ''' creates routing table levels 0-39
        within each level contains a map with keys representing 16
        hexadecimal digits and a list to hold values
        '''
        for i in range(40):
            prefix = self.node_id[:i]
            self.routing_table[prefix]={hex(j)[2:].upper(): [] for j in range(16)}


    def active_connections_check(self, connection_signal):
        ''' using backpointers to send periodic UDP broadcasts to
        nodes that allow verification neighbor link persists
        '''
        if True:
            return True
        else:
            return False
        # TCP timeouts?

    def remove_connection(self, connection_signal):
        ''' instead of costly reinsertion, mark invalid?
        '''
        pass

    def auth_validation(self, validate_signal) -> (bool,str):
        try:
            decoded_key = authenticationtype.decode(
                validate_signal,
                path_to_where_secret_key_is_stored,
                algorithmUsed
            )
            return True, decoded_key
        except ExpiredKeyError:
            return False, None
        else invalidTokenError:
            return False, None

    def route_to_node(self, dest_node, message):
        # include TTL, response
