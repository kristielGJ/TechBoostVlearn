# Use the mcr image repository as the base image
FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu

# Install Python and Node.js
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends python3.11 python3-pip \
    && curl -fsSL https://deb.nodesource.com/setup_21.x | bash - \
    && apt-get -y install --no-install-recommends nodejs=21.7.1-1nodesource1

# Set the working directory
WORKDIR /workspaces/TechBoostVlearn

# Install backend dependencies
COPY Backend/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Install frontend dependencies
COPY v-learn/package.json v-learn/package-lock.json v-learn/
RUN cd v-learn && npm ci

# Copy the entire project
COPY . .

# Start the backend and frontend
CMD ["pip", "install", "Flask", "flask-cors", "pdfminer.six", "chardet", "PyMuPDF"]
CMD ["npm", "start", "--prefix", "v-learn"]