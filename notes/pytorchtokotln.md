    To set up a **PyTorch model in a Kotlin project**, especially for mobile (Android), you typically use **PyTorch Mobile**. Here's a full guide to integrating a PyTorch model into your Kotlin-based Android project:

---

### ✅ Step-by-Step Guide to Setup PyTorch in Kotlin Project

#### **1. Convert Your PyTorch Model to `.pt` or `.ptl` Format**

Make sure your model is **traced or scripted** and exported using TorchScript:

```python
import torch

# Example model
model = MyModel()
model.eval()

# Dummy input for tracing
example_input = torch.rand(1, 3, 224, 224)
traced_script_module = torch.jit.trace(model, example_input)
traced_script_module.save("model.pt")  # or .ptl for Lite
```

---

#### **2. Add PyTorch Android Dependency**

Add the following dependencies to your `app/build.gradle`:

```groovy
dependencies {
    implementation 'org.pytorch:pytorch_android:1.13.1'
    implementation 'org.pytorch:pytorch_android_torchvision:1.13.1' // Optional, for image transforms
}
```

Check for the latest version on [PyTorch Android GitHub](https://github.com/pytorch/pytorch/tree/main/android).

---

#### **3. Place Model File in Assets Folder**

* Place `model.pt` or `model.ptl` in the `assets` directory:

```
app/src/main/assets/model.pt
```

---

#### **4. Load Model in Kotlin**

Here's an example in Kotlin using PyTorch Android API:

```kotlin
import org.pytorch.IValue
import org.pytorch.Module
import org.pytorch.Tensor
import org.pytorch.torchvision.TensorImageUtils
import android.graphics.Bitmap
import android.content.res.AssetManager

class PyTorchModel(private val assetManager: AssetManager) {
    private val module: Module = Module.load(assetFilePath("model.pt"))

    fun predict(bitmap: Bitmap): FloatArray {
        val inputTensor = TensorImageUtils.bitmapToFloat32Tensor(
            bitmap,
            TensorImageUtils.TORCHVISION_NORM_MEAN_RGB,
            TensorImageUtils.TORCHVISION_NORM_STD_RGB
        )

        val outputTensor = module.forward(IValue.from(inputTensor)).toTensor()
        return outputTensor.dataAsFloatArray
    }

    private fun assetFilePath(assetName: String): String {
        val file = File(context.filesDir, assetName)
        if (file.exists() && file.length() > 0) return file.absolutePath

        assetManager.open(assetName).use { inputStream ->
            FileOutputStream(file).use { outputStream ->
                val buffer = ByteArray(4 * 1024)
                var read:
```


android {
    // ...
    aaptOptions {
        noCompress "pt", "ptl"
    }
}
