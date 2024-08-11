//customIcons.ts
import { h } from "vue";
import type { IconSet, IconProps } from "vuetify";
import MiSTerIcon from "./customIconsSVG/MiSTerIcon.vue";

const customIcons: any = {
  MiSTerIcon,
};

const customIconSet: IconSet = {
  component: (props: IconProps) =>
    h(props.tag, [
      h(customIcons[props.icon as string], { class: "v-icon__svg" }),
    ]),
};

export { customIconSet /* aliases */ };
