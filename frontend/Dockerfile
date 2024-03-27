FROM node:20-alpine

ENV NEXT_TELEMETRY_DISABLED 1

WORKDIR /app

RUN apk add --no-cache libc6-compat

COPY . .

RUN npm ci
RUN npm run build

CMD ["npm", "run", "start"]