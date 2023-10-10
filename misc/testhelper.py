from util.base import *

class TestExpectation:
    EXPECTATION_FILES = {
        'angle_end2end_tests': ['src/tests/angle_end2end_tests_expectations.txt'],
        'info_collection_tests': ['content/test/gpu/gpu_tests/test_expectations/info_collection_expectations.txt'],
        'trace_test': ['content/test/gpu/gpu_tests/test_expectations/trace_test_expectations.txt'],
        'webgpu_cts_tests': [
            'third_party/dawn/webgpu-cts/expectations.txt',
            'third_party/dawn/webgpu-cts/slow_tests.txt'
        ],
    }

    # These expected failures are not in expectation files, which will be maintained locally and appended to expectation files or updated in test results.
    LOCAL_EXPECTATIONS = {
        'src/tests/angle_end2end_tests_expectations.txt': [
          'hsdes/18019513118 WIN INTEL D3D11 : SimpleStateChangeTest.DrawWithTextureTexSubImageThenDrawAgain/ES2_D3D11 = SKIP',
          'hsdes/18019513118 WIN INTEL D3D11 : SimpleStateChangeTest.UpdateTextureInUse/ES2_D3D11 = SKIP',
          # Windows RDP failures because Microsoft basic render is got.
          '0000 WIN D3D11 : EGLDisplaySelectionTestDeviceId.DeviceId/* = SKIP',
          '0000 WIN D3D11 : EGLDisplaySelectionTestDeviceId.DeviceIdConcurrently/* = SKIP',
          # Windows failures related to lock screen.
          '0000 WIN : GPUTestConfigTest.GPUTestConfigConditions_D3D11/ES2_D3D9 = SKIP',
          '0000 WIN : ProgramBinariesAcrossPlatforms.CreateAndReloadBinary/ES2_D3D11_to_ES2_D3D9 = SKIP',
          '0000 WIN : ProgramBinariesAcrossPlatforms.CreateAndReloadBinary/ES2_D3D9_to_ES2_D3D11 = SKIP',
        ],
        'content/test/gpu/gpu_tests/test_expectations/info_collection_expectations.txt': [
          # Windows failures related to RDP or lock screen.
          '[ win ] InfoCollection_direct_composition [ Failure ]'
        ],
        'content/test/gpu/gpu_tests/test_expectations/trace_test_expectations.txt': [
          # https://github.com/webatintel/webconformance/issues/24
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_MP4_FourColors_Rot_180 [ Failure ]',
          # Windows failures related to RDP or lock screen.
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Underlay [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Underlay_Fullsize [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_MP4 [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_MP4_BGRA [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_MP4_FourColors_Aspect_4x3 [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_MP4_FourColors_Rot_270 [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_MP4_FourColors_Rot_90 [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_MP4_Fullsize [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_MP4_NV12 [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_MP4_Rounded_Corner [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_MP4_VP_SCALING [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_MP4_YUY2 [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_SW_Decode [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_VP9 [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_VP9_BGRA [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_VP9_Fullsize [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_VP9_NV12 [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_VP9_VP_SCALING [ Failure ]',
          '[ win intel ] OverlayModeTraceTest_DirectComposition_Video_VP9_YUY2 [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Underlay [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_MP4 [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_MP4_FourColors_Aspect_4x3 [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_MP4_FourColors_Rot_180 [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_MP4_FourColors_Rot_270 [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_MP4_FourColors_Rot_90 [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_MP4_NV12 [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_MP4_Rounded_Corner [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_MP4_VP_SCALING [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_MP4_YUY2 [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_SW_Decode [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_VP9 [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_VP9_NV12 [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_VP9_VP_SCALING [ Failure ]',
          '[ win intel ] VideoPathTraceTest_DirectComposition_Video_VP9_YUY2 [ Failure ]',
        ],
        'third_party/dawn/webgpu-cts/expectations.txt': [
            'crbug.com/1301808 [ intel ubuntu ] webgpu:web_platform,canvas,configure:viewFormats:canvasType="onscreen";format="rgba16float";* [ Failure ]',
            'crbug.com/1301808 [ intel ubuntu ] webgpu:web_platform,canvas,configure:viewFormats:canvasType="offscreen";format="rgba16float";* [ Failure ]'
        ],
        # There is no expection file for dawn_end2end_tests. The expectations will be used to suppress the dawn e2e failures in test report.
        # Example: '[ Util.HOST_OS ] ComputeStorageBufferBarrierTests.UniformToStorageAddPingPong/D3D11_Intel_R_Arc_TM_A770_Graphics'
        'dawn_end2end_tests': [],
        'angle_white_box_tests': [
            # Windows failures related to RDP or lock screen.
            '[ win32 ] D3DTextureClearTest.ClearBGRA8/ES2_D3D9',
            '[ win32 ] D3DTextureClearTest.ClearR16/ES2_D3D9',
            '[ win32 ] D3DTextureClearTest.ClearR8/ES2_D3D9',
            '[ win32 ] D3DTextureClearTest.ClearRG16/ES2_D3D9',
            '[ win32 ] D3DTextureClearTest.ClearRG8/ES2_D3D9',
            '[ win32 ] D3DTextureClearTest.ClearRGB10A2/ES2_D3D9',
            '[ win32 ] D3DTextureClearTest.ClearRGBA8/ES2_D3D9',
            '[ win32 ] D3DTextureClearTest.ClearRGBAF16/ES2_D3D9',
            '[ win32 ] D3DTextureTest.BindTexImage/ES2_D3D9',
            '[ win32 ] D3DTextureTest.CheckSampleMismatch/ES2_D3D9',
            '[ win32 ] D3DTextureTest.Clear/ES2_D3D9',
            '[ win32 ] D3DTextureTest.DepthStencil/ES2_D3D9',
            '[ win32 ] D3DTextureTest.GlColorspaceNotAllowedForTypedD3DTexture/ES2_D3D9',
            '[ win32 ] D3DTextureTest.NonReadablePBuffer/ES2_D3D9',
            '[ win32 ] D3DTextureTest.NonRenderableTextureImage/ES2_D3D9',
            '[ win32 ] D3DTextureTest.RGBEmulationTextureImage/ES2_D3D9',
            '[ win32 ] D3DTextureTest.TestD3D11SupportedFormatsSurface/ES2_D3D9',
            '[ win32 ] D3DTextureTest.TestD3D11SupportedFormatsTexture/ES2_D3D9',
            '[ win32 ] D3DTextureTest.TestD3D11TypelessTexture/ES2_D3D9',
            '[ win32 ] D3DTextureTest.TextureArray/ES2_D3D9',
            '[ win32 ] D3DTextureTest.TypelessD3DTextureNotSupported/ES2_D3D9',
            '[ win32 ] D3DTextureTest.UnnecessaryWidthHeightAttributes/ES2_D3D9',
            '[ win32 ] D3DTextureYUVTest.NV12TextureImageReadPixel/ES2_D3D9',
            '[ win32 ] D3DTextureYUVTest.NV12TextureImageRender/ES2_D3D9',
            '[ win32 ] D3DTextureYUVTest.NV12TextureImageSampler/ES2_D3D9',
            '[ win32 ] D3DTextureYUVTest.P010TextureImageReadPixel/ES2_D3D9',
            '[ win32 ] D3DTextureYUVTest.P010TextureImageRender/ES2_D3D9',
            '[ win32 ] D3DTextureYUVTest.P010TextureImageSampler/ES2_D3D9',
            '[ win32 ] D3DTextureYUVTest.P016TextureImageReadPixel/ES2_D3D9',
            '[ win32 ] D3DTextureYUVTest.P016TextureImageRender/ES2_D3D9',
            '[ win32 ] D3DTextureYUVTest.P016TextureImageSampler/ES2_D3D9',
            '[ win32 ] EGLDirectCompositionTest.RenderSolidColor/ES2_D3D11_NoFixture',
            '[ win32 ] ErrorMessagesTest.ErrorMessages/ES2_D3D9',
        ],
    }

    # Match intel tag in the gpu tags, such as '[ webgpu-adapter-default intel ]',
    # '[ intel-gen-9 win10 ]' and '[ intel-0x9bc5 ]'.
    intel_tag_pattern = re.compile(r'intel\S*')

    @staticmethod
    def _update_gpu_tag(line, intel_expectations=[]):
        # Comment line
        if line.startswith('#'):
            return line

        # Get first matching tags, which may be gpu tags or may not.
        gpu_tags_match = re.search(r'\[.*?\]', line)
        if not gpu_tags_match:
            return line

        gpu_tags = gpu_tags_match.group()
        if TestExpectation.intel_tag_pattern.search(gpu_tags):
            # Replace 'intel*' with 'intel' in the gpu tags
            updated_gpu_tags = TestExpectation.intel_tag_pattern.sub('intel', gpu_tags)

            updated_line = line if updated_gpu_tags == gpu_tags else line.replace(gpu_tags, updated_gpu_tags)

            # If the updated line already exists, just comment the line,
            # otherwise comment the line and append the updated line.
            # For the line already with 'intel' tag, keep as is if there is no duplicate line.
            if updated_line in intel_expectations:
                line = '# ' + line
            else:
                if updated_gpu_tags != gpu_tags:
                    line =  '# ' + line + updated_line
                intel_expectations.append(updated_line)
        return line


    @staticmethod
    def update(target, root_dir):
        if not os.path.exists(root_dir):
            Util.warning(f'{root_dir} does not exist')
            return

        expectation_files = TestExpectation.EXPECTATION_FILES.get(target)
        if not expectation_files:
            return

        for expectation_file in expectation_files:
            file_path = f'{root_dir}/{expectation_file}'
            if not os.path.exists(file_path):
                Util.warning(f'{file_path} does not exist')
                return

            # Hold the expectations with the 'intel' tag for duplication check.
            # Because there may be some expectations with same case, but different device ids,
            # after the update, there will be duplicate record, which is not allowed.
            intel_expectations = []

            line_comment = '#'
            if target in ['angle_end2end_tests']:
                line_comment = '//'

            update_comment = f'{line_comment} LOCAL UPDATE FOR INTEL GPUS'
            has_update_comment = False
            tag_header_scope = True
            for line in fileinput.input(file_path, inplace=True):
                # Skip if the expectation file has been updated.
                if has_update_comment:
                    sys.stdout.write(line)
                    continue

                if fileinput.isfirstline():
                    if re.search(update_comment, line):
                        has_update_comment = True
                    else:
                        line = f'{update_comment}\n' + line

                if target in ['trace_test', 'webgpu_cts_tests']:
                    if tag_header_scope:
                        if re.search('END TAG HEADER', line):
                            tag_header_scope = False
                    else:
                        line = TestExpectation._update_gpu_tag(line, intel_expectations)
                sys.stdout.write(line)
            fileinput.close()

            # Append local expectations
            if has_update_comment:
                return
            append_expectations = TestExpectation.LOCAL_EXPECTATIONS.get(expectation_file)
            if append_expectations:
                expectations_str = ''
                for expectation in append_expectations:
                    if expectation not in intel_expectations:
                        expectations_str = expectations_str + f'{expectation}\n'
                if expectations_str != '':
                    f = open(file_path, 'a')
                    f.write(f'\n{line_comment} Locally maintained expectation items\n')
                    f.write(expectations_str)
                    f.close()

class TestResult:
    def __init__(self, result_file=None, real_type=None):
        self.pass_fail = []
        self.fail_pass = []
        self.fail_fail = []
        self.pass_pass = []

        if not result_file or not real_type:
            return

        try:
            json_result = json.load(open(result_file))

            if real_type in ['gtest_angle', 'telemetry_gpu_integration_test', 'webgpu_blink_web_tests']:
                for key, val in json_result['tests'].items():
                    self._parse_result(key, val, key)

            elif real_type == 'gtest_chrome':
                for key, val in json_result['per_iteration_data'][0].items():
                    if val[0]['status'] == 'SUCCESS':
                        self.pass_pass.append(key)
                    elif val[0]['status'] == 'FAILURE':
                        self.pass_fail.append(key)

            elif real_type == 'angle':
                errors_count = json_result['errors']
                failures_count = json_result['failures']
                pass_fail_count = errors_count + failures_count
                total_count = json_result['tests']
                pass_pass_count = total_count - pass_fail_count
                self.pass_pass = [0] * pass_pass_count
                if pass_fail_count:
                    self.pass_fail.append('%s in %s' % (pass_fail_count, result_file))

            elif real_type == 'dawn':
                for test_suite in json_result['testsuites']:
                    suite_name = test_suite['name']
                    for test in test_suite['testsuite']:
                        test_name = '%s.%s' % (suite_name, test['name'])
                        if 'failures' in test:
                            self.pass_fail.append(test_name)
                        else:
                            self.pass_pass.append(test_name)
        except Exception as e:
            self.pass_fail.append('All in %s' % result_file)

    def _parse_result(self, key, val, path):
        def _is_pass(val):
            return str(val).endswith('PASS')

        if 'expected' in val and 'actual' in val:
            expected_pass = _is_pass(val['expected'])
            actual_pass = _is_pass(val['actual'])
            if not expected_pass and not actual_pass:
                self.fail_fail.append(path)
            elif not expected_pass and actual_pass:
                self.fail_pass.append(path)
            elif expected_pass and not actual_pass:
                self.pass_fail.append(path)
            elif expected_pass and actual_pass:
                self.pass_pass.append(path)
        else:
            for new_key, new_val in val.items():
                self._parse_result(new_key, new_val, '%s/%s' % (path, new_key))
