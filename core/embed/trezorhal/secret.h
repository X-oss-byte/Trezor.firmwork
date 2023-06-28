
#include <stdint.h>
#include "secbool.h"

#define SECRET_HEADER_MAGIC "TRZS"
#define SECRET_HEADER_LEN 16
#define SECRET_OPTIGA_KEY_OFFSET 16
#define SECRET_OPTIGA_KEY_LEN 32

#define SECRET_MONOTONIC_COUNTER_OFFSET 48
#define SECRET_MONOTONIC_COUNTER_LEN 1024

secbool secret_bootloader_locked(void);

void secret_write(uint8_t* data, uint32_t offset, uint32_t len);

secbool secret_read(uint8_t* data, uint32_t offset, uint32_t len);

secbool secret_wiped(void);

void secret_erase(void);

void secret_hide(void);

void secret_write_header(void);
