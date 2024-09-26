plugins {
    kotlin("multiplatform") version "1.9.0"
    id("org.jetbrains.compose") version "1.5.0" // Подключение Compose Multiplatform
}

kotlin {
    js(IR) {
        browser {
            binaries.executable()
        }
    }
    sourceSets {
        val jsMain by getting {
            dependencies {
                implementation(compose.web.core)
                implementation(compose.runtime)
                implementation("io.github.kirillNay:tg-mini-app:1.1.0") // Подключение tg-mini-app
            }
        }
    }
}

compose.experimental {
    web.application {}
}

repositories {
    mavenCentral()
    google()
}
