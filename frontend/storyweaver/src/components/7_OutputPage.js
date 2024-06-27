import React from 'react';
import JSZip from 'jszip';
import { saveAs } from 'file-saver';

const images = [
  { src: './images/0_image.png', alt: 'Image 1', description: 'Description for Image 1' }, // 다운로드할 이미지 경로
  { src: './images/0_image.png', alt: 'Image 2', description: 'Description for Image 2' },
  { src: './images/0_image.png', alt: 'Image 3', description: 'Description for Image 3' },
  { src: './images/0_image.png', alt: 'Image 4', description: 'Description for Image 4' },
];

const OutputPage = () => {
  const downloadImage = (src) => {
    saveAs(src, src.split('/').pop());
  };

  const downloadAllImages = async () => {
    const zip = new JSZip();
    const imgFolder = zip.folder("images");

    for (const image of images) {
      const response = await fetch(image.src);
      const blob = await response.blob();
      imgFolder.file(image.src.split('/').pop(), blob);
    }

    zip.generateAsync({ type: "blob" }).then((content) => {
      saveAs(content, "./images/all_images.zip");
    });
  };

  return (
      <div className='content'>
        <h1>Checkout your generated images!</h1>
        <div className="content1">
            <p>Click the download buttons to download images.</p>
        </div>
        <div className='container'>
          <div className="image-list">
            {images.map((image, index) => (
              <div key={index} className="image-item">
                <img src={image.src} alt={image.alt} />
                <div className='image-details' >
                  <p> {image.description} </p>
                </div>
                <button onClick={() => downloadImage(image.src)} className="link-button">Download</button>
              </div>
            ))}
            <button onClick={downloadAllImages} className="link-button"> Download All as Zip</button>
          </div>
        </div>
      </div>
  );
};

export default OutputPage;
