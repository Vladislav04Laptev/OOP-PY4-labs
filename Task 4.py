class Animal:
    def __init__(self, ani_fam: str, ani_name: str, weight: (int, float), high: int):
        """
               Создание и подготовка к работе объекта "Животное"

               :param ani_fam: Семейство животных, к которым относится животное
               :param ani_name: Название животного
               :param weight: Вес животного в кг
               :param high: Рост животного в см

        """
        self._ani_fam = ani_fam #делаем непубличными, чтобы нельзя было изменить название семейства, в инкапсуляции проверяем корректность введенных данных
        self._ani_name = ani_name #делаем непубличными, чтобы нельзя было изменить название животного, в инкапсуляции проверяем корректность введенных данных
        self.weight = weight #в инкапсуляции проверяем корректность введенных данных
        self.high = high #в инкапсуляции проверяем корректность введенных данных

    @property
    def ani_fam(self) -> str:
        return self._ani_fam

    @property
    def ani_name(self) -> str:
        return self._ani_name

    @property
    def weight(self) -> (int, float):
        return self._weight

    @weight.setter
    def weight(self, new_weight: (int, float)):
        if not isinstance(new_weight, (int, float)):
            raise TypeError("Вес животного должен быть типа int или float ")
        if new_weight <= 0:
            raise ValueError("Вес животного должен быть положительным числом")
        self._weight = new_weight

    @property
    def high(self) -> int:
        return self._high

    @high.setter
    def high(self, new_high: int):
        if not isinstance(new_high, int):
            raise TypeError("Рост животного должен быть типа int")
        if new_high <= 0:
            raise ValueError("Рост животного должен быть положительным числом")
        self._high = new_high

    def high_multiply_weight(self) -> float:
        """
                Функция которая перемножает вес животного на его рост с точностью 1 знак после запятой

                :return: Вес * Рост

                Наследуется в дочерних классах
        """
        return round(self.high * self.weight, 1)

    def size(self) -> None:
        """
            Функция которая печатает размер животного по его весу и росту

            :return: None

            Перегружается в дочерние классы
        """
        if (self.weight > 300.0 and self.high > 300):
            print("Big animal")
            return None
        if (self.weight > 300.0 or self.high > 300):
            print("Middle animal")
            return None
        else:
            print("Small animal")
            return None

    def __str__(self): #наследуется в дочерних классах
        return f"Семейство животного: {self._ani_fam}. Название животного: {self._ani_name}. Вес: {self.weight} кг. Рост: {self.high} см"

    def __repr__(self): #наследуется в дочерних классах
        return f"{self.__class__.__name__}(ani_fam={self._ani_fam!r}, ani_name={self._ani_name!r}, weight={self.weight!r}, high={self.high!r})"

class Cat(Animal):
    def __init__(self, weight: (int, float), high: int):
        """
            Создание и подготовка к работе объекта "Кот"

            :param ani_fam: Кошачьи (постоянный атрибут класса)
            :param ani_name: Кот (постоянный атрибут класса)
            :param weight: Вес кота в кг
            :param high: Рост кота в см
        """
        self._ani_fam = "Кошачьи"
        self._ani_name = "Кот"
        super().__init__(self._ani_fam, self._ani_name, weight, high) #остальную часть берём из родительского класса

    def size(self) -> None: #перегружаем класс так как оценка размера котов отличается от оценки размеров животных
        """
            Функция которая печатает размер кота по его весу и росту

            :return: None
        """
        if (self.weight > 20.0 and self.high > 15):
            print("Big Cat")
            return None
        if (self.weight > 20.0 or self.high > 15):
            print("Middle Cat")
            return None
        else:
            print("Small Cat")
            return None

if __name__ == "__main__":
    Chupokabra = Animal("Чупокабровые", "Чупокабра", 15.1, 20)
    print(Chupokabra)
    print(repr(Chupokabra))
    print(Chupokabra.high_multiply_weight())
    Chupokabra.size()

    print("\n")

    Murzik = Cat(15.1, 20)
    print(Murzik)
    print(repr(Murzik))
    print(Murzik.high_multiply_weight())
    Murzik.size()
pass
