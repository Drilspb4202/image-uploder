# Simple Media Uploader

A lightweight, self-hosted image and video hosting service. Upload files and get direct links instantly.

## Features
- 🚀 **Fast Uploads**: Drag & drop interface.
- 📱 **Responsive Design**: Modern, glassmorphism UI.
- 📂 **Persistent Storage**: Files are saved directly to your server's filesystem.
- 🐳 **Docker Ready**: Easy deployment with Docker Compose or Coolify.

## Structure
- **API**: FastAPI (Python) backend handling file uploads.
- **Web**: Nginx serving the static frontend and proxying requests to the API.

---

## 🛠 Deployment Guide

### Option 1: Coolify (Recommended)

1. **Connect Repository**: Connect your GitHub repository to Coolify.
2. **Select Type**: Choose **Docker Compose** as the deployment type.
3. **Configuration**:
   - Coolify should automatically detect the `docker-compose.yaml`.
   - **Crucial Step**: Ensure the Volume Path exists.
     The `docker-compose.yaml` is configured to save files to:
     `/home/miron/radon/image-uploader/uploads`
     
     *If you are deploying on a different server or path, you must edit `docker-compose.yaml` to point to a valid directory on your server.*

4. **Deploy**: Click "Deploy".
5. **Access**: The application will be available on port `8090` of your server IP (e.g., `http://your-server-ip:8090`).

### Option 2: Manual Docker Compose

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Drilspb4202/image-uploder.git
   cd image-uploder
   ```

2. **Prepare the Upload Directory**:
   Ensure the upload path specified in `docker-compose.yaml` exists. By default, it is hardcoded to `/home/miron/radon/image-uploader/uploads`.
   
   If you are running this locally or on another machine, open `docker-compose.yaml` and change the volume mapping to a relative path:
   ```yaml
   volumes:
     - ./uploads:/data/uploads
   ```

3. **Run the container**:
   ```bash
   docker-compose up -d --build
   ```

4. **Access**:
   Open http://localhost:8090 in your browser.

## ⚙️ Configuration

### Storage Path
The storage location is defined in `docker-compose.yaml` under the `api` service:
```yaml
volumes:
  - /absolute/path/to/your/folder:/data/uploads
```
Change `/absolute/path/...` to wherever you want files to persist on the host machine.

### Ports
- **Frontend**: Exposed on port `8090` by default.
- **API**: Runs internally on port `8000`.

## 📝 Usage
1. Drag and drop an image or video onto the page.
2. Click **Upload to Server**.
3. Once uploaded, click the **Copy** button to get the direct link.
