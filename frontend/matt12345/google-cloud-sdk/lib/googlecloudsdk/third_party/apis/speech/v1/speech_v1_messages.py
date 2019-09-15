"""Generated message classes for speech version v1.

Converts audio to text by applying powerful neural network models.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'speech'


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class LongRunningRecognizeMetadata(_messages.Message):
  r"""Describes the progress of a long-running `LongRunningRecognize` call. It
  is included in the `metadata` field of the `Operation` returned by the
  `GetOperation` call of the `google::longrunning::Operations` service.

  Fields:
    lastUpdateTime: Time of the most recent processing update.
    progressPercent: Approximate percentage of audio processed thus far.
      Guaranteed to be 100 when the audio is fully processed and the results
      are available.
    startTime: Time when the request was received.
  """

  lastUpdateTime = _messages.StringField(1)
  progressPercent = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  startTime = _messages.StringField(3)


class LongRunningRecognizeRequest(_messages.Message):
  r"""The top-level message sent by the client for the `LongRunningRecognize`
  method.

  Fields:
    audio: *Required* The audio data to be recognized.
    config: *Required* Provides information to the recognizer that specifies
      how to process the request.
  """

  audio = _messages.MessageField('RecognitionAudio', 1)
  config = _messages.MessageField('RecognitionConfig', 2)


class LongRunningRecognizeResponse(_messages.Message):
  r"""The only message returned to the client by the `LongRunningRecognize`
  method. It contains the result as zero or more sequential
  `SpeechRecognitionResult` messages. It is included in the `result.response`
  field of the `Operation` returned by the `GetOperation` call of the
  `google::longrunning::Operations` service.

  Fields:
    results: Output only. Sequential list of transcription results
      corresponding to sequential portions of audio.
  """

  results = _messages.MessageField('SpeechRecognitionResult', 1, repeated=True)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class RecognitionAudio(_messages.Message):
  r"""Contains audio data in the encoding specified in the
  `RecognitionConfig`. Either `content` or `uri` must be supplied. Supplying
  both or neither returns google.rpc.Code.INVALID_ARGUMENT. See [content
  limits](https://cloud.google.com/speech-to-text/quotas#content).

  Fields:
    content: The audio data bytes encoded as specified in `RecognitionConfig`.
      Note: as with all bytes fields, proto buffers use a pure binary
      representation, whereas JSON representations use base64.
    uri: URI that points to a file that contains audio data bytes as specified
      in `RecognitionConfig`. The file must not be compressed (for example,
      gzip). Currently, only Google Cloud Storage URIs are supported, which
      must be specified in the following format:
      `gs://bucket_name/object_name` (other URI formats return
      google.rpc.Code.INVALID_ARGUMENT). For more information, see [Request
      URIs](https://cloud.google.com/storage/docs/reference-uris).
  """

  content = _messages.BytesField(1)
  uri = _messages.StringField(2)


class RecognitionConfig(_messages.Message):
  r"""Provides information to the recognizer that specifies how to process the
  request.

  Enums:
    EncodingValueValuesEnum: Encoding of audio data sent in all
      `RecognitionAudio` messages. This field is optional for `FLAC` and `WAV`
      audio files and required for all other audio formats. For details, see
      AudioEncoding.

  Fields:
    audioChannelCount: *Optional* The number of channels in the input audio
      data. ONLY set this for MULTI-CHANNEL recognition. Valid values for
      LINEAR16 and FLAC are `1`-`8`. Valid values for OGG_OPUS are '1'-'254'.
      Valid value for MULAW, AMR, AMR_WB and SPEEX_WITH_HEADER_BYTE is only
      `1`. If `0` or omitted, defaults to one channel (mono). Note: We only
      recognize the first channel by default. To perform independent
      recognition on each channel set
      `enable_separate_recognition_per_channel` to 'true'.
    enableAutomaticPunctuation: *Optional* If 'true', adds punctuation to
      recognition result hypotheses. This feature is only available in select
      languages. Setting this for requests in other languages has no effect at
      all. The default 'false' value does not add punctuation to result
      hypotheses. Note: This is currently offered as an experimental service,
      complimentary to all users. In the future this may be exclusively
      available as a premium feature.
    enableSeparateRecognitionPerChannel: This needs to be set to `true`
      explicitly and `audio_channel_count` > 1 to get each channel recognized
      separately. The recognition result will contain a `channel_tag` field to
      state which channel that result belongs to. If this is not true, we will
      only recognize the first channel. The request is billed cumulatively for
      all channels recognized: `audio_channel_count` multiplied by the length
      of the audio.
    enableWordTimeOffsets: *Optional* If `true`, the top result includes a
      list of words and the start and end time offsets (timestamps) for those
      words. If `false`, no word-level time offset information is returned.
      The default is `false`.
    encoding: Encoding of audio data sent in all `RecognitionAudio` messages.
      This field is optional for `FLAC` and `WAV` audio files and required for
      all other audio formats. For details, see AudioEncoding.
    languageCode: *Required* The language of the supplied audio as a
      [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag.
      Example: "en-US". See [Language Support](https://cloud.google.com
      /speech-to-text/docs/languages) for a list of the currently supported
      language codes.
    maxAlternatives: *Optional* Maximum number of recognition hypotheses to be
      returned. Specifically, the maximum number of
      `SpeechRecognitionAlternative` messages within each
      `SpeechRecognitionResult`. The server may return fewer than
      `max_alternatives`. Valid values are `0`-`30`. A value of `0` or `1`
      will return a maximum of one. If omitted, will return a maximum of one.
    metadata: *Optional* Metadata regarding this request.
    model: *Optional* Which model to select for the given request. Select the
      model best suited to your domain to get best results. If a model is not
      explicitly specified, then we auto-select a model based on the
      parameters in the RecognitionConfig. <table>   <tr>
      <td><b>Model</b></td>     <td><b>Description</b></td>   </tr>   <tr>
      <td><code>command_and_search</code></td>     <td>Best for short queries
      such as voice commands or voice search.</td>   </tr>   <tr>
      <td><code>phone_call</code></td>     <td>Best for audio that originated
      from a phone call (typically     recorded at an 8khz sampling
      rate).</td>   </tr>   <tr>     <td><code>video</code></td>     <td>Best
      for audio that originated from from video or includes multiple
      speakers. Ideally the audio is recorded at a 16khz or greater
      sampling rate. This is a premium model that costs more than the
      standard rate.</td>   </tr>   <tr>     <td><code>default</code></td>
      <td>Best for audio that is not one of the specific audio models.
      For example, long-form audio. Ideally the audio is high-fidelity,
      recorded at a 16khz or greater sampling rate.</td>   </tr> </table>
    profanityFilter: *Optional* If set to `true`, the server will attempt to
      filter out profanities, replacing all but the initial character in each
      filtered word with asterisks, e.g. "f***". If set to `false` or omitted,
      profanities won't be filtered out.
    sampleRateHertz: Sample rate in Hertz of the audio data sent in all
      `RecognitionAudio` messages. Valid values are: 8000-48000. 16000 is
      optimal. For best results, set the sampling rate of the audio source to
      16000 Hz. If that's not possible, use the native sample rate of the
      audio source (instead of re-sampling). This field is optional for FLAC
      and WAV audio files, but is required for all other audio formats. For
      details, see AudioEncoding.
    speechContexts: *Optional* array of SpeechContext. A means to provide
      context to assist the speech recognition. For more information, see
      [speech adaptation](https://cloud.google.com/speech-to-text/docs
      /context-strength).
    useEnhanced: *Optional* Set to true to use an enhanced model for speech
      recognition. If `use_enhanced` is set to true and the `model` field is
      not set, then an appropriate enhanced model is chosen if an enhanced
      model exists for the audio.  If `use_enhanced` is true and an enhanced
      version of the specified model does not exist, then the speech is
      recognized using the standard version of the specified model.
  """

  class EncodingValueValuesEnum(_messages.Enum):
    r"""Encoding of audio data sent in all `RecognitionAudio` messages. This
    field is optional for `FLAC` and `WAV` audio files and required for all
    other audio formats. For details, see AudioEncoding.

    Values:
      ENCODING_UNSPECIFIED: Not specified.
      LINEAR16: Uncompressed 16-bit signed little-endian samples (Linear PCM).
      FLAC: `FLAC` (Free Lossless Audio Codec) is the recommended encoding
        because it is lossless--therefore recognition is not compromised--and
        requires only about half the bandwidth of `LINEAR16`. `FLAC` stream
        encoding supports 16-bit and 24-bit samples, however, not all fields
        in `STREAMINFO` are supported.
      MULAW: 8-bit samples that compand 14-bit audio samples using G.711 PCMU
        /mu-law.
      AMR: Adaptive Multi-Rate Narrowband codec. `sample_rate_hertz` must be
        8000.
      AMR_WB: Adaptive Multi-Rate Wideband codec. `sample_rate_hertz` must be
        16000.
      OGG_OPUS: Opus encoded audio frames in Ogg container
        ([OggOpus](https://wiki.xiph.org/OggOpus)). `sample_rate_hertz` must
        be one of 8000, 12000, 16000, 24000, or 48000.
      SPEEX_WITH_HEADER_BYTE: Although the use of lossy encodings is not
        recommended, if a very low bitrate encoding is required, `OGG_OPUS` is
        highly preferred over Speex encoding. The [Speex](https://speex.org/)
        encoding supported by Cloud Speech API has a header byte in each
        block, as in MIME type `audio/x-speex-with-header-byte`. It is a
        variant of the RTP Speex encoding defined in [RFC
        5574](https://tools.ietf.org/html/rfc5574). The stream is a sequence
        of blocks, one block per RTP packet. Each block starts with a byte
        containing the length of the block, in bytes, followed by one or more
        frames of Speex data, padded to an integral number of bytes (octets)
        as specified in RFC 5574. In other words, each RTP header is replaced
        with a single byte containing the block length. Only Speex wideband is
        supported. `sample_rate_hertz` must be 16000.
    """
    ENCODING_UNSPECIFIED = 0
    LINEAR16 = 1
    FLAC = 2
    MULAW = 3
    AMR = 4
    AMR_WB = 5
    OGG_OPUS = 6
    SPEEX_WITH_HEADER_BYTE = 7

  audioChannelCount = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  enableAutomaticPunctuation = _messages.BooleanField(2)
  enableSeparateRecognitionPerChannel = _messages.BooleanField(3)
  enableWordTimeOffsets = _messages.BooleanField(4)
  encoding = _messages.EnumField('EncodingValueValuesEnum', 5)
  languageCode = _messages.StringField(6)
  maxAlternatives = _messages.IntegerField(7, variant=_messages.Variant.INT32)
  metadata = _messages.MessageField('RecognitionMetadata', 8)
  model = _messages.StringField(9)
  profanityFilter = _messages.BooleanField(10)
  sampleRateHertz = _messages.IntegerField(11, variant=_messages.Variant.INT32)
  speechContexts = _messages.MessageField('SpeechContext', 12, repeated=True)
  useEnhanced = _messages.BooleanField(13)


class RecognitionMetadata(_messages.Message):
  r"""Description of audio data to be recognized.

  Enums:
    InteractionTypeValueValuesEnum: The use case most closely describing the
      audio content to be recognized.
    MicrophoneDistanceValueValuesEnum: The audio type that most closely
      describes the audio being recognized.
    OriginalMediaTypeValueValuesEnum: The original media the speech was
      recorded on.
    RecordingDeviceTypeValueValuesEnum: The type of device the speech was
      recorded with.

  Fields:
    audioTopic: Description of the content. Eg. "Recordings of federal supreme
      court hearings from 2012".
    industryNaicsCodeOfAudio: The industry vertical to which this speech
      recognition request most closely applies. This is most indicative of the
      topics contained in the audio.  Use the 6-digit NAICS code to identify
      the industry vertical - see https://www.naics.com/search/.
    interactionType: The use case most closely describing the audio content to
      be recognized.
    microphoneDistance: The audio type that most closely describes the audio
      being recognized.
    obfuscatedId: Obfuscated (privacy-protected) ID of the user, to identify
      number of unique users using the service.
    originalMediaType: The original media the speech was recorded on.
    originalMimeType: Mime type of the original audio file.  For example
      `audio/m4a`, `audio/x-alaw-basic`, `audio/mp3`, `audio/3gpp`. A list of
      possible audio mime types is maintained at
      http://www.iana.org/assignments/media-types/media-types.xhtml#audio
    recordingDeviceName: The device used to make the recording.  Examples
      'Nexus 5X' or 'Polycom SoundStation IP 6000' or 'POTS' or 'VoIP' or
      'Cardioid Microphone'.
    recordingDeviceType: The type of device the speech was recorded with.
  """

  class InteractionTypeValueValuesEnum(_messages.Enum):
    r"""The use case most closely describing the audio content to be
    recognized.

    Values:
      INTERACTION_TYPE_UNSPECIFIED: Use case is either unknown or is something
        other than one of the other values below.
      DISCUSSION: Multiple people in a conversation or discussion. For example
        in a meeting with two or more people actively participating. Typically
        all the primary people speaking would be in the same room (if not, see
        PHONE_CALL)
      PRESENTATION: One or more persons lecturing or presenting to others,
        mostly uninterrupted.
      PHONE_CALL: A phone-call or video-conference in which two or more
        people, who are not in the same room, are actively participating.
      VOICEMAIL: A recorded message intended for another person to listen to.
      PROFESSIONALLY_PRODUCED: Professionally produced audio (eg. TV Show,
        Podcast).
      VOICE_SEARCH: Transcribe spoken questions and queries into text.
      VOICE_COMMAND: Transcribe voice commands, such as for controlling a
        device.
      DICTATION: Transcribe speech to text to create a written document, such
        as a text-message, email or report.
    """
    INTERACTION_TYPE_UNSPECIFIED = 0
    DISCUSSION = 1
    PRESENTATION = 2
    PHONE_CALL = 3
    VOICEMAIL = 4
    PROFESSIONALLY_PRODUCED = 5
    VOICE_SEARCH = 6
    VOICE_COMMAND = 7
    DICTATION = 8

  class MicrophoneDistanceValueValuesEnum(_messages.Enum):
    r"""The audio type that most closely describes the audio being recognized.

    Values:
      MICROPHONE_DISTANCE_UNSPECIFIED: Audio type is not known.
      NEARFIELD: The audio was captured from a closely placed microphone. Eg.
        phone, dictaphone, or handheld microphone. Generally if there speaker
        is within 1 meter of the microphone.
      MIDFIELD: The speaker if within 3 meters of the microphone.
      FARFIELD: The speaker is more than 3 meters away from the microphone.
    """
    MICROPHONE_DISTANCE_UNSPECIFIED = 0
    NEARFIELD = 1
    MIDFIELD = 2
    FARFIELD = 3

  class OriginalMediaTypeValueValuesEnum(_messages.Enum):
    r"""The original media the speech was recorded on.

    Values:
      ORIGINAL_MEDIA_TYPE_UNSPECIFIED: Unknown original media type.
      AUDIO: The speech data is an audio recording.
      VIDEO: The speech data originally recorded on a video.
    """
    ORIGINAL_MEDIA_TYPE_UNSPECIFIED = 0
    AUDIO = 1
    VIDEO = 2

  class RecordingDeviceTypeValueValuesEnum(_messages.Enum):
    r"""The type of device the speech was recorded with.

    Values:
      RECORDING_DEVICE_TYPE_UNSPECIFIED: The recording device is unknown.
      SMARTPHONE: Speech was recorded on a smartphone.
      PC: Speech was recorded using a personal computer or tablet.
      PHONE_LINE: Speech was recorded over a phone line.
      VEHICLE: Speech was recorded in a vehicle.
      OTHER_OUTDOOR_DEVICE: Speech was recorded outdoors.
      OTHER_INDOOR_DEVICE: Speech was recorded indoors.
    """
    RECORDING_DEVICE_TYPE_UNSPECIFIED = 0
    SMARTPHONE = 1
    PC = 2
    PHONE_LINE = 3
    VEHICLE = 4
    OTHER_OUTDOOR_DEVICE = 5
    OTHER_INDOOR_DEVICE = 6

  audioTopic = _messages.StringField(1)
  industryNaicsCodeOfAudio = _messages.IntegerField(2, variant=_messages.Variant.UINT32)
  interactionType = _messages.EnumField('InteractionTypeValueValuesEnum', 3)
  microphoneDistance = _messages.EnumField('MicrophoneDistanceValueValuesEnum', 4)
  obfuscatedId = _messages.IntegerField(5)
  originalMediaType = _messages.EnumField('OriginalMediaTypeValueValuesEnum', 6)
  originalMimeType = _messages.StringField(7)
  recordingDeviceName = _messages.StringField(8)
  recordingDeviceType = _messages.EnumField('RecordingDeviceTypeValueValuesEnum', 9)


class RecognizeRequest(_messages.Message):
  r"""The top-level message sent by the client for the `Recognize` method.

  Fields:
    audio: *Required* The audio data to be recognized.
    config: *Required* Provides information to the recognizer that specifies
      how to process the request.
  """

  audio = _messages.MessageField('RecognitionAudio', 1)
  config = _messages.MessageField('RecognitionConfig', 2)


class RecognizeResponse(_messages.Message):
  r"""The only message returned to the client by the `Recognize` method. It
  contains the result as zero or more sequential `SpeechRecognitionResult`
  messages.

  Fields:
    results: Output only. Sequential list of transcription results
      corresponding to sequential portions of audio.
  """

  results = _messages.MessageField('SpeechRecognitionResult', 1, repeated=True)


class SpeechContext(_messages.Message):
  r"""Provides "hints" to the speech recognizer to favor specific words and
  phrases in the results.

  Fields:
    phrases: *Optional* A list of strings containing words and phrases "hints"
      so that the speech recognition is more likely to recognize them. This
      can be used to improve the accuracy for specific words and phrases, for
      example, if specific commands are typically spoken by the user. This can
      also be used to add additional words to the vocabulary of the
      recognizer. See [usage limits](https://cloud.google.com/speech-to-
      text/quotas#content).  List items can also be set to classes for groups
      of words that represent common concepts that occur in natural language.
      For example, rather than providing phrase hints for every month of the
      year, using the $MONTH class improves the likelihood of correctly
      transcribing audio that includes months.
  """

  phrases = _messages.StringField(1, repeated=True)


class SpeechOperationsGetRequest(_messages.Message):
  r"""A SpeechOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class SpeechOperationsListRequest(_messages.Message):
  r"""A SpeechOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class SpeechProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A SpeechProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class SpeechProjectsLocationsOperationsListRequest(_messages.Message):
  r"""A SpeechProjectsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class SpeechRecognitionAlternative(_messages.Message):
  r"""Alternative hypotheses (a.k.a. n-best list).

  Fields:
    confidence: Output only. The confidence estimate between 0.0 and 1.0. A
      higher number indicates an estimated greater likelihood that the
      recognized words are correct. This field is set only for the top
      alternative of a non-streaming result or, of a streaming result where
      `is_final=true`. This field is not guaranteed to be accurate and users
      should not rely on it to be always provided. The default of 0.0 is a
      sentinel value indicating `confidence` was not set.
    transcript: Output only. Transcript text representing the words that the
      user spoke.
    words: Output only. A list of word-specific information for each
      recognized word. Note: When `enable_speaker_diarization` is true, you
      will see all the words from the beginning of the audio.
  """

  confidence = _messages.FloatField(1, variant=_messages.Variant.FLOAT)
  transcript = _messages.StringField(2)
  words = _messages.MessageField('WordInfo', 3, repeated=True)


class SpeechRecognitionResult(_messages.Message):
  r"""A speech recognition result corresponding to a portion of the audio.

  Fields:
    alternatives: Output only. May contain one or more recognition hypotheses
      (up to the maximum specified in `max_alternatives`). These alternatives
      are ordered in terms of accuracy, with the top (first) alternative being
      the most probable, as ranked by the recognizer.
    channelTag: For multi-channel audio, this is the channel number
      corresponding to the recognized result for the audio from that channel.
      For audio_channel_count = N, its output values can range from '1' to
      'N'.
  """

  alternatives = _messages.MessageField('SpeechRecognitionAlternative', 1, repeated=True)
  channelTag = _messages.IntegerField(2, variant=_messages.Variant.INT32)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details.  You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class WordInfo(_messages.Message):
  r"""Word-specific information for recognized words.

  Fields:
    endTime: Output only. Time offset relative to the beginning of the audio,
      and corresponding to the end of the spoken word. This field is only set
      if `enable_word_time_offsets=true` and only in the top hypothesis. This
      is an experimental feature and the accuracy of the time offset can vary.
    startTime: Output only. Time offset relative to the beginning of the
      audio, and corresponding to the start of the spoken word. This field is
      only set if `enable_word_time_offsets=true` and only in the top
      hypothesis. This is an experimental feature and the accuracy of the time
      offset can vary.
    word: Output only. The word corresponding to this set of information.
  """

  endTime = _messages.StringField(1)
  startTime = _messages.StringField(2)
  word = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
