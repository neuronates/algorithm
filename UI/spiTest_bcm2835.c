#include <bcm2835.h> //Library for the bcm2835
#include <stdio.h>
#include <stdlib.h>

//define GPIO PIN Numbers

#define RESET RPI_GPIO_P1_11
#define PWDN RPI_GPIO_P1_12
#define START RPI_GPIO_P1_15
#define DRDY RPI_GPIO_P1_16
#define CLKSEL RPI_GPIO_P1_18
#define SDATAC 0x11

//------------------------------------------------


int main(int argc, char **argv){


          //load library

         if((bcm2835_init())<0){
                printf("Could not load the bcm2835 library \n");
                exit(1);
         }
         printf("Library loaded \n");

         //Set GPIO Pins to Output

         bcm2835_gpio_fsel(RESET,BCM2835_GPIO_FSEL_OUTP);
         bcm2835_gpio_fsel(PWDN,BCM2835_GPIO_FSEL_OUTP);
         bcm2835_gpio_fsel(START,BCM2835_GPIO_FSEL_OUTP);
         bcm2835_gpio_fsel(DRDY,BCM2835_GPIO_FSEL_OUTP);
         bcm2835_gpio_fsel(CLKSEL,BCM2835_GPIO_FSEL_OUTP);

         //initiate SPI
         bcm2835_spi_begin();
         bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);
         bcm2835_spi_setDataMode(BCM2835_SPI_MODE1);
         bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_65536);
         bcm2835_spi_chipSelect(BCM2835_SPI_CS0);
         bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, LOW);


         // POWERUP Sequenz S.58, FIG 56
         // ALL INPUTS LOW
         bcm2835_gpio_write(RESET,LOW);
         bcm2835_gpio_write(PWDN,LOW);
         bcm2835_gpio_write(START,LOW);
         bcm2835_gpio_write(DRDY,LOW);

         bcm2835_gpio_write(CLKSEL,LOW);
         // CLKSEL -> 1 , wait
         bcm2835_gpio_write(CLKSEL,HIGH);
         bcm2835_delay(500);
         // PDWN -> 1, RESET -> 1, wait 1s
         bcm2835_gpio_write(PWDN, HIGH);
         bcm2835_gpio_write(RESET,HIGH);
         bcm2835_delay(1000);
         // RESET PULSE
         bcm2835_gpio_write(RESET,LOW);
         bcm2835_delay(50);
         bcm2835_gpio_write(RESET,HIGH);

         printf("Power-Up Done \n");
         bcm2835_delay(50);
         // send SDATAC
         int error;
         error = bcm2835_spi_transfer(SDATAC);

         printf("SDATAC sent \n");

         //set Internal Reference
         char write[] = { 0x43 , 0x00 , 0xE0 };
         bcm2835_spi_transfern(write, sizeof(write));

         printf("Internal Reference set \n");

         //Read Register
         char read[] = { 0x20 , 0x00, 0x00, 0x00 };
         bcm2835_spi_transfern(read, sizeof(read));
         printf("Data Read: %X , %X \n", read[0], read[1]);
         //Close Device
         bcm2835_spi_end();
         bcm2835_close();
         printf("bye bye \n");
         return 0;
}
