// PAM
#include "DSK6713_aic23.h"
Uint32 fs=DSK6713_AIC23_FREQ_8KHZ;
#include <math.h>
//Initialization:
int i_PAM;
int j_PAM;
int k;
int masked_value, output;
int data_4PAM[4] = {0x7FFF, 0x2AAA, -0x2AAB, -0x8000};
int out_buffer[256];
int i=0;
interrupt void c_int11() //interrupt service routine
{
int sample_data;
if (i_PAM==96)
{
sample_data = input_sample(); //inputs data
i_PAM=0;
j_PAM=0;
}
masked_value = sample_data & 0x0003;
output = data_4PAM[masked_value];
output_sample(output);
out_buffer[i++] = output;
if (i==256)
i = 0;
j_PAM++; //repeated output counter
if (j_PAM==12)
{
j_PAM=0;
 sample_data = sample_data >> 2;
}
i_PAM++;
return;
}
void main()
{
i_PAM=0;
comm_intr(); //init DSK, codec, McBSP
while(1); //infinite loop
}
