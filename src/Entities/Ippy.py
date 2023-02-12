from Reader import Reader


class Ippy:

    def __init__(self, ip, cidr):
        self.ip = ip
        self.cidr = int(cidr)
        self.ip_binary_arr = []
        self.cidr_binary_arr = []
        self.ip_network_binary_arr = []
        self.dic_decimal_binary = Reader.read_json_file("decimal_binary/decimal_binary.json")
        self.output = {}

    def __str__(self):
        return f'{self.ip}/{self.cidr}'

    def ip_to_binary(self):
        ip_array = self.ip.split('.')
        for decimal in ip_array:
            binary_ip = self.dic_decimal_binary[decimal]
            for binary in binary_ip:
                self.ip_binary_arr.append(int(binary))
            self.ip_binary_arr.append('.')
        self.ip_binary_arr = self.ip_binary_arr[:-1]
        # self.ip_binary_arr = '.'.join(str(bin) for bin in ip_binary)

    def cidr_to_binary(self):
        count = 0
        while len(self.cidr_binary_arr) < 35:
            if count % 8 == 0 and count != 0:
                self.cidr_binary_arr.append(".")
            if count >= self.cidr:
                self.cidr_binary_arr.append(0)
            else:
                self.cidr_binary_arr.append(1)
            count += 1

    def calcul_sum_bit(self, int1, int2):
        if int1 == 1 and int2 == 1:
            return 1
        else:
            return 0


    def get_network_ip(self):
        for n, z in zip(self.ip_binary_arr, self.cidr_binary_arr):
            if n == '.' or z == '.':
                self.ip_network_binary_arr.append('.')
            else:
                self.ip_network_binary_arr.append(self.calcul_sum_bit(n, z))

    def convert_to_binary(self):
        self.ip_to_binary()
        self.cidr_to_binary()
        self.get_network_ip()

    def get_details(self):
        self.convert_to_binary()
        return {
            "ip": self.__str__(),
            "bin_ip": self.ip_binary_arr,
            "bin_cidr": self.cidr_binary_arr,
            "bin_network_ip": self.ip_network_binary_arr
            }


if __name__ == '__main__':
    MyIp = Ippy("10.102.161.64", "26")
    ip_details = MyIp.get_details()
    print("Details", ip_details)

