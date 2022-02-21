FROM node:14-alpine AS deps

WORKDIR /app/

COPY ./package.json ./yarn.lock ./

RUN yarn install


FROM node:14-alpine AS builder

WORKDIR /app

COPY . .

COPY --from=deps /app/node_modules ./node_modules

EXPOSE 3000

CMD ["yarn", "dev"]
