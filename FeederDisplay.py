import drivers

class FeederDisplay:
  def __init__(self, feeder):
    print('init FeederDisplay')
    self.feeder = feeder
    self.display = drivers.Lcd()

  def render(self):
    display = self.display
    feeder = self.feeder

    display.lcd_clear()
    display.lcd_display_string("Mahlzeit!", 1)
    display.lcd_display_string("Futterausgabe:", 2)
    display.lcd_display_string(str(round(feeder.feedingAmount)) + " Gramm (" + str(round(feeder.feedingDuration,2)) + 's)', 3)

    if feeder.isFeeding:
        display.lcd_display_string("Fuetterung...",4)
    else:
        display.lcd_display_string("Betriebsbereit.",4)