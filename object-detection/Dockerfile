ARG FUNCTION_DIR="/home/app/"

FROM python:3-slim-buster AS python-alpine
FROM python-alpine AS build-image

# Include global args in this stage of the build
ARG FUNCTION_DIR
# Create function directory
RUN mkdir -p ${FUNCTION_DIR}
# Copy handler function
COPY . ${FUNCTION_DIR}
RUN python3 -m pip install boto3 awslambdaric --target ${FUNCTION_DIR}

FROM python-alpine
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}
CMD [ "python3", "-m", "awslambdaric", "app.lambda_handler" ]