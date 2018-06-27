import fileinput

class Kiko():
    
    def entrada(self):
        usuario = list()
        for line in fileinput.input():
            usuario.append(line)
        return usuario

    def salida(self, usuario):
        
        index = 0
        while index < len(usuario):
            n = int(usuario[index].strip(' \t\r\n').split(' ')[1])
            if n == 0:
                break
            index += 1
            numbers_list = list()
            numbers_dict = dict()
            strip_line = usuario[index].strip(' \t\r\n')
            index += 1
            for x in strip_line.split():
                number = int(x)
                numbers_list.append(number)
                numbers_dict[number] = 0
            b = self.result(numbers_list, n, numbers_dict)
            if b == -1:
                print('impossivel')
            else:
                print(b)

    def euclidean(self, a, b):
        
        a_max = max(a, b)
        b_min = min(a, b)
        if b_min == 0:
            return a_max
        return self.euclidean(b_min, a_max % b_min)

    def get(self, a, n, numbers_dict):
        
        for i in range(2, n + 1):
            if i in numbers_dict:
                continue
            mcd = self.euclidean(a, i)
            if mcd == -1:
                continue
            if (a * i) / mcd == n:
                return i
        return -1

    def mcm(self, a, b):
        
        return (a * b) / self.euclidean(a, b)

    def result(self, numbers_list, n, numbers_dict):
        
        for i in numbers_list:
            if n % i != 0:
                return -1
        index = 0
        a = numbers_list[index]
        index += 1
        while index < len(numbers_list):
            b = numbers_list[index]
            index += 1
            a = self.mcm(a, b)
        return self.get(a, n, numbers_dict)

if __name__ == '__main__':
    hk = Kiko()
    usuario = hk.entrada()
    hk.salida(usuario)