<script setup lang="ts">
import { mistertaptorom } from "@/utils";
import { type SimpleRom } from "@/stores/roms.js";

// Props
const props = defineProps<{ rom: SimpleRom }>();

</script>

<template>
    <v-btn
    :disabled="!rom.mister_path"
    @click.stop="mistertaptorom(props.rom)"
    variant="text"
    rounded="0"
    >
        <v-icon>customIconSet:MiSTerIcon</v-icon>
    </v-btn>
</template>