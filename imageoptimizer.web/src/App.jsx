import { useState } from 'react'
import './App.css'

function App() {
  const [selectedImage, setSelectedImage] = useState(null)
  const [quality, setQuality] = useState(80)
  const [processedImage, setProcessedImage] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (!selectedImage) {
      alert('Please select an image first')
      return
    }

    const formData = new FormData()
    formData.append('image', selectedImage)
    formData.append('quality', quality)

    try {
      const response = await fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData,
      })

      if (response.ok) {
        const blob = await response.blob()
        const imageUrl = URL.createObjectURL(blob)

        console.log(imageUrl)

        setProcessedImage(imageUrl)
      } else {
        const errorText = await response.text()
        console.error('Upload failed:', errorText)
        alert('Upload failed')
      }
    } catch (error) {
      console.error('Error:', error)
      alert('Something went wrong')
    }
  }

  return (
    <div className="container">
      <h1>Image Optimizer</h1>

      <form onSubmit={handleSubmit}>
        {/* Upload */}
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setSelectedImage(e.target.files[0])}
        />

        {/* Quality Slider */}
        <div>
          <label>Quality: {quality}</label>
          <input
            type="range"
            min="0"
            max="100"
            value={quality}
            onChange={(e) => setQuality(parseInt(e.target.value))}
          />
        </div>

        <button type="submit">Optimize Image</button>
      </form>

      {processedImage && (
        <div style={{ marginTop: '20px' }}>
          <h3>Processed Image:</h3>
          <img
            src={processedImage}
            alt="Processed"
            style={{ maxWidth: '300px', borderRadius: '8px' }}
          />
        </div>
      )}
    </div>
  )
}

export default App