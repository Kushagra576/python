class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3


    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.min_volume
        self.__channel = Television.min_channel 

    def power(self):
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
        
    def mute(self):
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False


    def channel_up(self):
        if self.__status == True:
            if self.__channel == self.max_channel:
                self.__channel = self.min_channel
            else:
                self.__channel += 1
    
    def channel_down(self):
        if self.__status == True:
            if self.__channel == self.min_channel:
                self.__channel = self.max_channel
            else:
                self.__channel -= 1

    def volume_up(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False

            if self.__volume < self.max_volume:
                self.__volume += 1

    def volume_down(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False

            if self.__volume > Television.min_volume:
                self.__volume -= 1
    
    def __str__(self):
        if self.__muted == True:
            shown_volume = 0
        else:
            shown_volume = self.__volume

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {shown_volume}'