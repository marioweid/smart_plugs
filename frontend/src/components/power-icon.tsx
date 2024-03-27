type PowerIconProps = {
    color: string,
}

function PowerIcon(props: PowerIconProps) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="40"
      height="40"
      fill="None"
      stroke="currentColor"
      viewBox="0 0 24 24"
    >
      <path
        stroke={props.color}
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="2"
        d="M12 7v5M8 9a5 5 0 108 0m5 3a9 9 0 11-18 0 9 9 0 0118 0z"
      ></path>
    </svg>
  );
}

export default PowerIcon;
