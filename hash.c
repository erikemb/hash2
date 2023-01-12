#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

#define ba 16
#define bo 10
#define n 4000

int main()
{
    int i;
    char input[ba + 1], output[bo + 1], temp[65], shain[17], shaout[17];
    int arm1[n][3], hash1[n/2][3], hash11[n/2], hash2[n/2][3], hash22[n/2];
    int addr[n], outs[n], m = n / 2, a = (int)ceil(log2(n) / 4);
    double tax;
    SHA256_CTX ctx;

    for(i = 0; i < n; i++)
    {
        addr[i] = rand() % (1 << ba);
        outs[i] = rand() % (1 << bo);
    }

    for(i = 0; i < n; i++)
    {
        snprintf(input, sizeof(input), "%d", addr[i]);
        SHA256_Init(&ctx);
        SHA256_Update(&ctx, input, strlen(input));
        SHA256_Final(temp, &ctx);

        for(int j = 0; j < 32; j++)
            sprintf(&temp[j*2], "%02x", temp[j]);

        strncpy(shain, temp, a);
        strncpy(shaout, temp + (32 - a), a);
        shain[a] = '\0';
        shaout[a] = '\0';
        arm1[i][0] = (int)strtol(shain, NULL, 16);
        arm1[i][1] = outs[i];
        arm1[i][2] = (int)strtol(shaout, NULL, 16);
    }

    for(i = 0; i < n; i++)
    {
        if(!(i in hash11) && (sizeof(hash1) < m))
        {
            hash11[i] = arm1[i][0];
            memcpy(hash1[i], arm1[i], sizeof(arm1[i]));
        }
    }

    for(i = 0; i < n; i++)
    {
        if(!(i in hash1) && !(i in hash22) && (sizeof(hash2) < m))
        {
            hash22[i] = arm1[i][0];
            memcpy(hash2[i], arm1[i], sizeof(arm1[i]));
        }
    }

    for(i = 0; i < sizeof(hash1); i++)
        printf("%d %d %d\n", hash1[i][0], hash1[i][1], hash1[i][2]);

    printf("\n");

    for(i = 0; i < sizeof(hash2); i++)
        printf("%d %d %d\n", hash2[i][0], hash2[i][1], hash2[i][2]);

    printf("\n");

    tax =
