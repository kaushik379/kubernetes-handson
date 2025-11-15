# -------- Build Stage --------
FROM node:20-alpine AS build
WORKDIR /usr/src/app

COPY package*.json ./
COPY . .

RUN yarn install --frozen-lockfile
RUN yarn build


# -------- Runtime Stage --------
FROM public.ecr.aws/amazonlinux/amazonlinux:2023

RUN dnf --setopt=install_weak_deps=False install -q -y \
    nodejs20 \
    shadow-utils \
    && \
    dnf clean all

RUN alternatives --install /usr/bin/node node /usr/bin/node-20 90

# Removed:
# ENV APPUSER=appuser
# ENV APPUID=1000
# ENV APPGID=1000
# RUN useradd ...

WORKDIR /app

# No chown needed since root owns everything by default
COPY --from=build /usr/src/app/node_modules ./node_modules
COPY --from=build /usr/src/app/dist ./dist

ENTRYPOINT [ "node", "dist/main.js" ]
