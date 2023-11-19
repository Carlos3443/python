class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''
        This method contains the instance variables that will be used in this program.
        '''
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        '''
        This method changes the instance variable 'self.__status' from True to False and False to True
        '''
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False

    def mute(self):
        '''
        This method changes the instance variable 'self.__muted' from True to False and False to True
        '''
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            elif self.__muted == True:
                self.__muted = False
        else:
            pass
    
    def channel_up(self):
        '''
        This method raises the instance variable 'self.__channel' by one if called, and if 'self.__channel' is already 3, it sets the variable to 0
        '''
        if self.__status == True:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL
        else:
            pass
    
    def channel_down(self):
        '''
        This method lowers the instance variable 'self.__channel' by one if called, and if 'self.__channel' is already 0, it sets the variable to 3
        '''
        if self.__status == True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            pass
    
    def volume_up(self):
        '''
        This method raises the instance variable 'self.__volume' by one if called, and if 'self.__volume' is already 2, it keeps the variable at 2
        '''
        if self.__status == True:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = self.MAX_VOLUME
        else:
            pass

    def volume_down(self):
        '''
        This method lowers the instance variable 'self.__volume' by one if called, and if 'self.__volume' is already 0, it keeps the variable at 0
        '''
        if self.__status == True:
            self.__muted = False
            if self.__volume == self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume -= 1
        else:
            pass

    def __str__(self) -> str:
        '''
        :return: This method returns the values of 'self.__status', 'self.__channel', and 'self.__volume' in a formatted string
        '''
        if self.__muted == True and self.__status == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
